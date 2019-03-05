import sys
import string
import threading
import redis
import pickle
from twisted.internet import defer
from twisted.internet import protocol
from twisted.internet import reactor
from twisted.python import log
from time import sleep

MORTPROD_HOST = '[server host]'
MORTPROD_PORT = 20001

REDIS_HOST = 'localhost'
REDIS_PORT = 6379

class ProxyServer(protocol.Protocol):


    def connectionMade(self):
        self.srv_queue = defer.DeferredQueue()
        self.cli_queue = defer.DeferredQueue()
        self.srv_queue.get().addCallback(self.clientDataReceived)

        factory = ProxyServerFactory(self.srv_queue, self.cli_queue)
        reactor.connectTCP(MORTPROD_HOST, MORTPROD_PORT, factory)
        reactor.suggestThreadPoolSize(30)

    def clientDataReceived(self, chunk):
        #log.msg("Server: writing %d bytes to original client" % len(chunk))
        #log.msg("res:")
        #self.hexdump(chunk)
        self.transport.write(chunk)
        self.srv_queue.get().addCallback(self.clientDataReceived)


    def dataReceived(self, chunk):
        #log.msg("Server: %d bytes received" % len(chunk))
        #log.msg("req:")
        #self.hexdump(chunk)
        self.cli_queue.put(chunk)

    def connectionLost(self, why):
        log.msg("stop connection from protocol")
        self.cli_queue.put(False)
        self.factory.closeConnection()

    def hexdump(self, src, length=16, sep='.'):
        DISPLAY = string.digits + string.letters + string.punctuation
        FILTER = ''.join(((x if x in DISPLAY else '.') for x in map(chr, range(256))))
        lines = []
        for c in xrange(0, len(src), length):
            chars = src[c:c + length]
            hex = ' '.join(["%02x" % ord(x) for x in chars])
            if len(hex) > 24:
                hex = "%s %s" % (hex[:24], hex[24:])
            printable = ''.join(["%s" % FILTER[ord(x)] for x in chars])
            lines.append("%08x:  %-*s  |%s|\n" % (c, length * 3, hex, printable))
        print ''.join(lines)


globalCache = {}
hittingCacheCounter = 0
notHittingCacheCounter = 0
hittingCacheCounterIteration = 0
notHittingCacheCounterIteration = 0

class ProxyServerProtocol(protocol.Protocol):

    reqChunk = None

    def connectionMade(self):
        log.msg("Client: connected to peer")
        self.cli_queue = self.factory.cli_queue
        self.cli_queue.get().addCallback(self.serverDataReceived)

    def serverDataReceived(self, chunk):
        log.msg("req:")
        self.hexdump(chunk)
        self.reqChunk = chunk
        if chunk is False:
            self.cli_queue = None
            log.msg("Client: disconnecting from peer")
            self.factory.continueTrying = False
            self.transport.loseConnection()
        elif self.cli_queue:
            # log.msg("Client: writing %d bytes to peer" % len(chunk))
            #log.msg("calling mortprod %d #" % self.callCounter)
            r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, decode_responses=True)
            cache_res = r.get(chunk)
            if cache_res is not None:
                unpacked_object = pickle.loads(cache_res)
                global hittingCacheCounter
                global hittingCacheCounterIteration
                hittingCacheCounter += 1
                hittingCacheCounterIteration += 1
                log.msg("Hitting cache :)")
                for cache_Chunk in unpacked_object:
                    self.dataReceived(cache_Chunk)
                    self.cli_queue.get().addCallback(self.serverDataReceived)
            else:
                global notHittingCacheCounter
                global notHittingCacheCounterIteration
                notHittingCacheCounter += 1
                notHittingCacheCounterIteration += 1
                self.transport.write(chunk)
                self.cli_queue.get().addCallback(self.serverDataReceived)
        else:
            self.factory.cli_queue.put(chunk)

    def dataReceived(self, chunk):
        #log.msg("Client: %d bytes received from peer" % len(chunk))
        #log.msg("***CHUNK***")
        log.msg("res:")
        self.hexdump(chunk)
        hexa = ":".join("{:02x}".format(ord(c)) for c in chunk[-7:-4])
        log.msg(hexa)
        self.setCache(chunk)
        if hexa == '00:02:00' or hexa == '00:09:00':   # END OF TCP IN SYBASE
            log.msg("OUT")
        self.factory.srv_queue.put(chunk)

    def setCache(self, chunk):
        if chunk is False:
            return
        r = redis.StrictRedis(REDIS_HOST, REDIS_PORT, decode_responses=True)
        cache_res = r.get(self.reqChunk)
        if cache_res is None:
            cache_res = []
        else:
            cache_res = pickle.loads(cache_res)
        if chunk not in cache_res:
            cache_res.append(chunk)
        pickled_object = pickle.dumps(cache_res)
        r.set(self.reqChunk, pickled_object)

    def connectionLost(self, why):
        if self.cli_queue:
            self.cli_queue = None
            #log.msg("Client: peer disconnected unexpectedly")

    def hexdump(self, src, length=16, sep='.'):
        DISPLAY = string.digits + string.letters + string.punctuation
        FILTER = ''.join(((x if x in DISPLAY else '.') for x in map(chr, range(256))))
        lines = []
        try:
            for c in xrange(0, len(src), length):
                chars = src[c:c + length]
                hex = ' '.join(["%02x" % ord(x) for x in chars])
                if len(hex) > 24:
                    hex = "%s %s" % (hex[:24], hex[24:])
                printable = ''.join(["%s" % FILTER[ord(x)] for x in chars])
                lines.append("%08x:  %-*s  |%s|\n" % (c, length * 3, hex, printable))
            print ''.join(lines)
        except TypeError:
            print src


class ProxyServerFactory(protocol.ReconnectingClientFactory):
    maxDelay = 10
    continueTrying = True
    protocol = ProxyServerProtocol

    def __init__(self, srv_queue, cli_queue):
        self.srv_queue = srv_queue
        self.cli_queue = cli_queue


class PauseAndStoreTransport(protocol.Protocol):

    def __init__(self, addr):
        self.addr = addr

    def makeConnection(self, transport):
        transport.pauseProducing()
        self.factory.addPausedTransport(transport, self.addr)


class ExternalServerFactory(protocol.ReconnectingClientFactory):

    maxConnections = 3
    currentConnections = 0
    transports = []
    goodOldProtocol = None

    def __init__(self):
        self.currentConnections = 0

    def buildProtocol(self, addr):
        if self.goodOldProtocol is None:
            self.goodOldProtocol = self.protocol

        if self.currentConnections < self.maxConnections:
            log.msg("Less them max connections")
            self.currentConnections += 1
            self.protocol = self.goodOldProtocol
            return protocol.ReconnectingClientFactory.buildProtocol(self, addr)
        log.msg("More them max connections - pausing...")
        self.protocol = PauseAndStoreTransport(addr)
        self.protocol.factory = self
        return self.protocol

    def addPausedTransport(self, transport, addr):
        self.transports.append((self.protocol, transport, addr))

    def closeConnection(self):
        global notHittingCacheCounterIteration
        global hittingCacheCounterIteration
        log.msg("Calls %d | Hittin cache: %d | not Hitting cache %d" %
                (hittingCacheCounterIteration + notHittingCacheCounterIteration, hittingCacheCounterIteration, notHittingCacheCounterIteration))
        notHittingCacheCounterIteration = 0
        hittingCacheCounterIteration = 0
        log.msg("Total - calls %d | hittin cache: %d | not hitting cache %d" %
                (hittingCacheCounter + notHittingCacheCounter, hittingCacheCounter, notHittingCacheCounter))
        log.msg("release one connections")
        self.currentConnections -= 1
        if self.currentConnections < self.maxConnections:
            log.msg("resuming queue connection")
            if len(self.transports) > 0:
                log.msg("queue not empty")
                originalProtocol, transport, addr = self.transports.pop(0)
                newProtocol = self.buildProtocol(addr)

                originalProtocol.dataReceived = newProtocol.dataReceived
                originalProtocol.connectionLost = newProtocol.connectionLost

                newProtocol.makeConnection(transport)
                transport.resumeProducing()


if __name__ == "__main__":


    log.startLogging(sys.stdout)
    factory = ExternalServerFactory()
    factory.protocol = ProxyServer
    reactor.listenTCP(19191, factory, interface="0.0.0.0")
    reactor.suggestThreadPoolSize(30)
    reactor.run()
