# -*- coding: utf-8 -*-
# pylint: disable=E0401
import logging
from google.cloud import texttospeech
import requests
import os
import time

class htts:


    def convert(self, text):
        url = '{}{}'.format(os.environ['HTTS_URL'],text) 
        res = requests.get(url)
        
        out_path = 'resources/output/res-{}.mp3'.format(str(int(time.time())))
        # The response's audio_content is binary.
        with open(out_path , 'wb') as out:
            out.write(res.content)
            logging.debug('Audio content written to file "output.mp3"')
        
        return out_path
