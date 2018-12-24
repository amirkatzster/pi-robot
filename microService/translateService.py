# -*- coding: utf-8 -*-
import logging
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
import pika
from services.queue import queue
from services.translate import translate
from services.cache import cache
from services.logger import setLogger
import os, shutil

class translateService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME_H2E = 'translateServiceH2E'
    QUEUE_NAME_E2H = 'translateServiceE2H'

    def __init__(self):
        setLogger('translateService')
        dotenv_path = '.env'
        load_dotenv(dotenv_path)
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME_H2E)
        self.channel.queue_declare(queue=self.QUEUE_NAME_E2H)
        self.channel.basic_consume(self.callback_h2e,
                      queue=self.QUEUE_NAME_H2E,
                      no_ack=True)
        self.channel.basic_consume(self.callback_e2h,
                      queue=self.QUEUE_NAME_E2H,
                      no_ack=True)
        self.translate = translate()
        self.cache = cache()
        
        
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        

    def callback_h2e(self, ch, method, properties, body):
        cacheKey = 'H2E|{}'.format(body)
        eng_text = self.cache.get(cacheKey)
        if (eng_text):
            logging.info('use cache')
        else:
            logging.info('[-h2e] {}'.format(body))
            logging.info('[+h2e] {}'.format(eng_text))
            self.cache.set(cacheKey, eng_text)
        self.channel.basic_publish(self.EXCHANGE_NAME,'dialogFlowService',eng_text)
        eng_text = self.translate.heb_to_eng(body)

    def callback_e2h(self, ch, method, properties, body):
        cacheKey = 'E2H|{}'.format(body)
        heb_text = self.cache.get(cacheKey)
        if (heb_text):
            logging.info('use cache')
        else:
            logging.info('[-e2h] {}'.format(body))
            heb_text = self.translate.eng_to_heb(body)
            logging.info('[+e2h] {}'.format(heb_text[::-1].encode('utf-8')))
        self.channel.basic_publish(self.EXCHANGE_NAME,'HebTextToSpeachService',heb_text)
        self.cache.set(cacheKey, heb_text)


if __name__ == "__main__":
    translateService().run()
        
        




