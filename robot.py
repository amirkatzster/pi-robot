from services.tts import tts
from services.translate import translate
from services.stt import stt
from services.record import record
from services.dialogflow import dialogflow
from services.play import play

class robot:

    def __init__(self):
        self.record = record()
        self.tts = tts()
        self.translate = translate()
        self.stt = stt()
        self.dialogflow = dialogflow()
        self.play = play()

    def main(self):
        #loop

        #record
        record_path = self.record.go()
        #stt
        heb_text_list = self.stt.convert(record_path)
        #translate
        eng_text_list = []
        for heb_text in heb_text_list:
            for alternative in heb_text.alternatives:
                text = alternative.transcript
                eng_text_list.append(self.translate.heb_to_eng(text))

        #dialogflow
        fulfillemnts = self.dialogflow.detect_intent_texts(1,eng_text_list)

        #tts
        full_text = '. '.join(fulfillemnts)
        print('robot going to say:')
        print(full_text)
        output_path = self.tts.convert(full_text)

        #play mp3
        self.play.start(output_path)
        


if __name__ == "__main__":
    robot().main()
    
