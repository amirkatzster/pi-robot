# -*- coding: utf-8 -*-
import logging
import pika
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
from services.queue import queue
from services.htts import htts
from services.play import play
from services.logger import setLogger
import os, shutil
import time

class hebTextToSpeachService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'HebTextToSpeachService'

    def __init__(self):
        setLogger('HebTextToSpeachService')
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        self.htts = htts()
        self.play = play()
        
        
       
        
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        

    def callback(self, ch, method, properties, body):
        logging.info('[-] {}'.format(body))
        output_path = self.htts.convert(body)
        logging.info('[+playing] {}'.format(output_path))
        # need to stop recording... 
        self.play.start(output_path)
        time.sleep(10)

        


if __name__ == "__main__":
    hebTextToSpeachService().run()
        
        




