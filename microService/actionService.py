import logging
import pika
from services.queue import queue
from services.logger import setLogger
from services.actionHandler import actionHandler
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
import os, shutil

class actionService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'actionService'

    def __init__(self):
        setLogger('actionService')
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        self.actionHandler = actionHandler()
        
    def run(self):
        while True:
            try:
                print(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()
            except Exception as e:
                logging.error(e)
        

    def callback(self, ch, method, properties, body):
        logging.info('[-] {}'.format(body))
        action = body.split('|')
        logging.info(action)
        self.actionHandler.process(action[0],action[1])

if __name__ == "__main__":
    actionService().run()
        
        




