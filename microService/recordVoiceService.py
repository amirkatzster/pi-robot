import logging
import pika
from services.record import record
from services.queue import queue
import os, shutil

class recordVoiceService:

    RECORDING_FOLDER = 'resources/records' 
    EXCHANGE_NAME = 'robo-pi' 
    QUEUE_NAME = 'recordVoiceService'
    shouldRecord = True

    def __init__(self):
        self.record = record()
        self.queue = queue()
        self.channel = self.queue.createChannel()
        self.channel.queue_declare(queue=self.QUEUE_NAME)
        # todo delete record folder
        self.deletePreviousRecords()
        # log to rabbit
        self.channel.basic_consume(self.callback,
                      queue=self.QUEUE_NAME,
                      no_ack=True)
        
       
        
    def run(self): 
        while (self.shouldRecord):     
            outputPath = self.record.record_by_silence()
            self.channel.basic_publish(self.EXCHANGE_NAME,'textToSpeachService',outputPath)



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
    # try:
        recordVoiceService().run()
    # except:
    #     logging.error('voice record service crashed :(',exc_info=True)
        
        




