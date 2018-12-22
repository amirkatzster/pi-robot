import logging
import pika
from services.queue import queue
from services.dialogflow import dialogflow
import os, shutil

class dialogFlowService:

    EXCHANGE_NAME = 'robo-pi' 
    QUEUE_NAME = 'dialogFlowService'

    def __init__(self):
        print(type(self).__name__)
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
        fulfillemnts = self.dialogflow.detect_intent_texts(2,texts)
        full_text = '. '.join(fulfillemnts)
        logging.info(full_text)
        self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceE2H',full_text)



if __name__ == "__main__":
    dialogFlowService().run()
        
        




