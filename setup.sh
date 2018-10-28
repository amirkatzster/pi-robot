#!/bin/sh
 pip install gTTS
 pip install urllib3
 pip install pydub

 pip install pafy
pip install -U python-dotenv

#record
sudo apt-get install portaudio19-dev
python -m pip install pyaudio

#stt
pip install --upgrade google-cloud-speech
export GOOGLE_APPLICATION_CREDENTIALS=/home/pi/git/pi-robot/Hidden/robot-pi-d6c05e651bc4.json

#translate
pip install --upgrade google-cloud-translate

#tts
pip install --upgrade google-cloud-texttospeech

#dialogflow
pip install dialogflow
 
#play 
pip install python-vlc

sudo apt-get install espeak
sudo apt-get install espeak python-espeak
