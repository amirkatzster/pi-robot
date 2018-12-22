import logging
import pika
from services.queue import queue
from services.translate import translate
import os, shutil

class translateService:

    EXCHANGE_NAME = 'robo-pi' 
    QUEUE_NAME_H2E = 'translateServiceH2E'
    QUEUE_NAME_E2H = 'translateServiceE2H'

    def __init__(self):
        print(type(self).__name__)
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
        
        
       
        
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        

    def callback_h2e(self, ch, method, properties, body):
        # caching needed
        eng_text = self.translate.heb_to_eng(body)
        self.channel.basic_publish(self.EXCHANGE_NAME,'dialogFlowService',eng_text)


    def callback_e2h(self, ch, method, properties, body):
        #caching
        heb_text = self.translate.eng_to_heb(body)
        logging.info(heb_text[::-1])
        self.channel.basic_publish(self.EXCHANGE_NAME,'HebTextToSpeachService',heb_text)


if __name__ == "__main__":
    translateService().run()
        
        




