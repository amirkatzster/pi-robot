# -*- coding: utf-8 -*-
# pylint: disable=E0401
import logging
from google.cloud import texttospeech
import requests
import os

class htts:

    OUTPUT_PATH = 'resources/output.mp3'

    def convert(self, text):
        url = '{}{}'.format(os.environ['HTTS_URL'],text) 
        res = requests.get(url)

        # The response's audio_content is binary.
        with open(self.OUTPUT_PATH , 'wb') as out:
            out.write(res.content)
            logging.debug('Audio content written to file "output.mp3"')
        
        return self.OUTPUT_PATH
