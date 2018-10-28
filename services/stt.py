import io
import os

# pylint: disable=E0401
# Imports the Google Cloud client library
from google.cloud import speech
from google.cloud.speech import enums
from google.cloud.speech import types

class stt:

    def __init__(self):
        self.client = speech.SpeechClient()

    def convert(self, file_name):
        # The name of the audio file to transcribe
        # file_name = os.path.join(
        #     os.path.dirname(__file__),
        #     'resources',
        #     'hiheb.wav')

        # Loads the audio into memory
        with io.open(file_name, 'rb') as audio_file:
            content = audio_file.read()
            audio = types.RecognitionAudio(content=content)

        config = types.RecognitionConfig(
            encoding=enums.RecognitionConfig.AudioEncoding.LINEAR16,
            sample_rate_hertz=44000,
            language_code='he-IL')

        # Detects speech in the audio file
        response = self.client.recognize(config, audio)
        print('response {}'.format(response))
        for result in response.results:
            print('Transcript: {}'.format(result.alternatives[0].transcript.encode('utf-8')))
        return response.results
