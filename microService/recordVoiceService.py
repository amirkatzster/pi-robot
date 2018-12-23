import logging
import pika
import sys
from services.record import record
from services.queue import queue
import os, shutil

class recordVoiceService:

    RECORDING_FOLDER = 'resources/records' 
    EXCHANGE_NAME = '' 
    QUEUE_NAME = 'recordVoiceService'
    shouldRecord = True

    def __init__(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        handler = logging.FileHandler('logs/recordVoiceService.log')
        handler.setLevel(logging.INFO)
        root.addHandler(ch)
        root.addHandler(handler)
        self.record = record()
        self.queue = queue()
        self.channel = self.queue.createChannel()
        #self.channel.queue_declare(queue=self.QUEUE_NAME)
        # todo delete record folder
        self.deletePreviousRecords()
        # log to rabbit
        #self.channel.basic_consume(self.callback,
        #              queue=self.QUEUE_NAME,
        #              no_ack=True)
        
       
        
    def run(self): 
        while (self.shouldRecord):     
            logging.info('---starting to record---')
            outputPath = self.record.record_by_silence()
            logging.info('---done recording---')
            channel = self.queue.createChannel()
            channel.basic_publish(self.EXCHANGE_NAME,'speachToTextService',outputPath)



    def deletePreviousRecords(self):
        folder = self.RECORDING_FOLDER
        if not os.path.exists(folder):
            os.makedirs(folder)
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
            except Exception as e:
                print(e)

    def callback(self, ch, method, properties, body):
        print(" [x] %r" % body)


if __name__ == "__main__":
    recordVoiceService().run()



