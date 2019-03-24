import logging
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
import pika
from services.queue import queue
from services.stt import stt
from services.logger import setLogger
import os, shutil

class speachToTextService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'speachToTextService'

    def __init__(self):
        setLogger('SpeachToTextService')
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        self.stt = stt()
        
        
       
        
    def run(self):
        while True:
            try:
                print(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()
            except Exception as e:
                logging.error(e)
        

    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)
        logging.info('file path: {}'.format(body))
        heb_text_list = self.stt.convert(body)
        logging.info('input text: {}'.format(heb_text_list))
        if not heb_text_list:
            logging.warn('Dont understand')
            ### Make flashes ###
        for heb_text in heb_text_list:
            for alternative in heb_text.alternatives:
                text = alternative.transcript
                logging.info(text[::-1])
                self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceH2E',text)
        


if __name__ == "__main__":
    speachToTextService().run()
        
        




