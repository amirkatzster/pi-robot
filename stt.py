import io
import os

# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class CloudSpeachToText:

    client = speech.SpeechClient()
    def Convert(self, file_name):
        # Instantiates a client
        print('client started')
        # The name of the audio file to transcribe
        # file_name = os.path.join(
        #     os.path.dirname(__file__),
        #     'resources',
        #     'hiheb.wav')

        print('file in {}'.format(file_name))
        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=16000,
            language_code='he-IL')

        # Detects speech in the audio file
        response = self.client.recognize(config, audio)
        print('response {}'.format(response))
        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript))
        return response.results
