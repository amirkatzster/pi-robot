from google.cloud import texttospeech

class tts:

    OUTPUT_PATH = 'resources/output.mp3'

    def __init__(self):
        self.client = texttospeech.TextToSpeechClient()

    def convert(self, text):
        #input_text = texttospeech.types.SynthesisInput(text=u'שלום לכולם')
        #input_text = texttospeech.types.SynthesisInput(text=u'Hi all testing the voice capabilities')
        input_text = texttospeech.types.SynthesisInput(text=text)

        # Note: the voice can also be specified by name.
        # Names of voices can be retrieved with client.list_voices().
        voice = texttospeech.types.VoiceSelectionParams(
            language_code='en-US',
            ssml_gender=texttospeech.enums.SsmlVoiceGender.FEMALE)

        audio_config = texttospeech.types.AudioConfig(
            audio_encoding=texttospeech.enums.AudioEncoding.MP3)

        response = self.client.synthesize_speech(input_text, voice, audio_config)

        # The response's audio_content is binary.
        with open(self.OUTPUT_PATH , 'wb') as out:
            out.write(response.audio_content)
            print('Audio content written to file "output.mp3"')
        
        return self.OUTPUT_PATH