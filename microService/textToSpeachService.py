import logging
import pika
from services.queue import queue
from services.htts import htts
from services.play import play
import os, shutil
import time

class textToSpeachService:

    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'textToSpeachService'

    def __init__(self):
        print(type(self).__name__)
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
        print(" [x] %r" % body)
        output_path = self.htts.convert(body)
        self.play.start(output_path)
        time.sleep(10)

        


if __name__ == "__main__":
    textToSpeachService().run()
        
        




