import logging
import pika
from services.queue import queue
from services.stt import stt
import os, shutil

class textToSpeachService:

    EXCHANGE_NAME = 'robo-pi' 
    QUEUE_NAME = 'textToSpeachService'

    def __init__(self):
        print(type(self).__name__)
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        self.stt = stt()
        
        
       
        
    def run(self):
        print(' [*] Waiting for messages. To exit press CTRL+C')
        self.channel.start_consuming()
        

    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)
        heb_text_list = self.stt.convert(body)
        logging.info('input text: {}'.format(heb_text_list))
        if not heb_text_list:
            logging.warn('Dont understand')
            ### Make flashes ###
        for heb_text in heb_text_list:
            for alternative in heb_text.alternatives:
                text = alternative.transcript
                logging.debug(text[::-1])
                self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceH2E',text)
        


if __name__ == "__main__":
    textToSpeachService().run()
        
        




