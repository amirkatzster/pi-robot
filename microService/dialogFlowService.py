import logging
import pika
from services.queue import queue
from services.dialogflow import dialogflow
from services.logger import setLogger
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
import os, shutil

class dialogFlowService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'dialogFlowService'

    def __init__(self):
        setLogger('dialogFlowService')
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        self.dialogflow = dialogflow()
        
        
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        

    def callback(self, ch, method, properties, body):
        # caching needed
        texts = []
        texts.append(body)
        logging.info('[-] {}'.format(texts))
        fulfillemnts = self.dialogflow.detect_intent_texts(2,texts)
        full_text = '. '.join(fulfillemnts)
        logging.info('[+] {}'.format(full_text))
        self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceE2H',full_text)



if __name__ == "__main__":
    dialogFlowService().run()
        
        




