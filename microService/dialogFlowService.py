import logging
import pika
from services.queue import queue
from services.dialogflow import dialogflow
from services.logger import setLogger
from os.path import join, dirname
from dotenv import load_dotenv, find_dotenv 
import os, shutil
from datetime import datetime, timedelta
import uuid

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
        self.sessionLast = datetime.now()
        self.sessionId = str(uuid.uuid4())
        
    def run(self):
        while True:
            try:
                print(' [*] Waiting for messages. To exit press CTRL+C')
                self.channel.start_consuming()
            except Exception as e:
                logging.error(e)

    def callback(self, ch, method, properties, body):
        # caching needed
        texts = []
        texts.append(body)
        logging.info('[-] {}'.format(texts))
        res = self.dialogflow.detect_intent_texts(self.getSessionId(),texts)
        full_text = '. '.join(res["say"])
        logging.info('[+say] {}'.format(full_text))
        self.channel.basic_publish(self.EXCHANGE_NAME,'translateServiceE2H',full_text)
        if (res["action"]):
            logging.info('[+action] {}'.format(res["action"]))
            self.channel.basic_publish(self.EXCHANGE_NAME, 'actionService',res["action"])

    def getSessionId(self):
        now = datetime.now()
        elapsed = now - self.sessionLast
        # after 2 minutes of non talking start new session
        if (elapsed > timedelta(minutes=2)):
            self.sessionId = str(uuid.uuid4())
        return self.sessionId

        


if __name__ == "__main__":
    dialogFlowService().run()
        
        




