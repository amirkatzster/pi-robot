from os.path import join, dirname
from dotenv import load_dotenv
from services.tts import tts
from services.translate import translate
from services.stt import stt
from services.record import record
from services.dialogflow import dialogflow
from services.play import play
from espeak import espeak


class robot:

    def __init__(self):
        dotenv_path = join(dirname(__file__), '.env')
        load_dotenv(dotenv_path)
        self.record = record()
        self.tts = tts()
        self.translate = translate()
        self.stt = stt()
        self.dialogflow = dialogflow()
        self.play = play()

    def main(self):
        #loop
        while True:
            #record
            #record_path = self.record.record_by_seconds()
            record_path = self.record.record_by_silence()
            #stt
            heb_text_list = self.stt.convert(record_path)
            #translate
            eng_text_list = []
            for heb_text in heb_text_list:
                for alternative in heb_text.alternatives:
                    text = alternative.transcript
                    print(text[::-1])
                    eng_text_list.append(self.translate.heb_to_eng(text))

            #dialogflow
            fulfillemnts = self.dialogflow.detect_intent_texts(2,eng_text_list)

            #tts
            full_text = '. '.join(fulfillemnts)
            print('robot going to say:')
            print(full_text)
            #heb_response = self.translate.eng_to_heb(full_text)
            #print(heb_response[::-1])
            #espeak.synth(full_text)
            output_path = self.tts.convert(full_text)

            #play mp3
            self.play.start(output_path)

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
        



if __name__ == "__main__":
    #robot().testRecord()
    #robot().testDialogFlow()
    #robot().readText()
    robot().main()
    
    
