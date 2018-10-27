from os.path import join, dirname
from dotenv import load_dotenv
from services.tts import tts
from services.htts import htts
from services.translate import translate
from services.stt import stt
from services.record import record
from services.dialogflow import dialogflow
from services.play import play
from services.led import led
import logging
import sys
import time

class robot:

    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.record = record()
        self.tts = tts()
        self.htts = htts()
        self.translate = translate()
        self.stt = stt()
        self.dialogflow = dialogflow()
       	self.play = play()
        self.led = led()
    
    def setLogger(self):
        root = logging.getLogger()
        root.setLevel(logging.DEBUG)
        ch = logging.StreamHandler(sys.stdout)
        ch.setLevel(logging.DEBUG)
        #formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        formatter = logging.Formatter('%(asctime)s - %(message)s')
        ch.setFormatter(formatter)
        root.addHandler(ch)

    def main(self):
        self.setLogger()
        #loop
        while True:
            self.led.turnRedOff()
            #record
            #record_path = self.record.record_by_seconds()
            record_path = self.record.record_by_silence()
            self.led.turnRedOn()
            #stt
            heb_text_list = self.stt.convert(record_path)
            #translate
            if not heb_text_list:
                output_path = self.htts.convert('')
                self.play.start(output_path)
                logging.debug('I hear silent.. Speak louder')
                continue
            eng_text_list = []
            for heb_text in heb_text_list:
                for alternative in heb_text.alternatives:
                    text = alternative.transcript
                    logging.debug(text[::-1])
                    eng_text_list.append(self.translate.heb_to_eng(text))

            #dialogflow
            fulfillemnts = self.dialogflow.detect_intent_texts(2,eng_text_list)

            #tts
            full_text = '. '.join(fulfillemnts)
            logging.debug('robot going to say:')
            logging.debug('full_text')
            heb_response = self.translate.eng_to_heb(full_text)
            print(heb_response[::-1])
            
            #migth be time optimization... To use synth voice.. 
            #espeak.synth(full_text)
            #output_path = self.tts.convert(full_text)
            output_path = self.htts.convert(heb_response)

            #play mp3
            self.play.start(output_path)
            time.sleep(3)
            #input("Press Enter to continue...")
    
    def testDialogFlow(self):
        #self.dialogflow.detect_intent_texts(1,['read me a book'])
        self.dialogflow.detect_intent_texts(1,['read me a book','Space book'])

    def testRecord(self):
        path = self.record.record_by_silence()
        print(path)

    def readText(self):
        output_path = self.tts.convert('Shlvm lchvlm n hrvvvt hchdsh shlchm tm rvtzm shnlch lshchk')
        self.play.start(output_path)

    def readTextHeb(self):
        
        output_path = self.htts.convert('')
        #output_path = 'resources/output.mp3'
        self.play.start(output_path)
        time.sleep(10)
        



if __name__ == "__main__":
    #robot().testRecord()
    #robot().testDialogFlow()
    #robot().readText()
    #robot().readTextHeb()
    robot().main()
    
    
