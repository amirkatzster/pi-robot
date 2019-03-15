import logging
import pika
from services.logger import setLogger

class queue:

    def createChannel(self):
        setLogger('queue')
        while (True):
            try:
                connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
                channel = connection.channel()
                return channel
            except Exception as e:
                logging.error('error connecting to queue' + str(e))      
