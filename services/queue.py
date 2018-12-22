import logging
import pika

class queue:

    def createChannel(self):
        connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
        return connection.channel()

    
        