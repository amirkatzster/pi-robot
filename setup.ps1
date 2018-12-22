 pip install gTTS
 pip install urllib3
 pip install pydub
 pip install pafy
 pip install python-dotenv


#record
python -m pip install pyaudio

#stt
pip install --upgrade google-cloud-speech
$env:GOOGLE_APPLICATION_CREDENTIALS="$((Get-Item -Path ".\").FullName)\Hidden\robot-pi-d6c05e651bc4.json"
$env:PYTHONPATH=c:\dev\GitHub\pi-robot

#translate
pip install --upgrade google-cloud-translate

#tts
pip install --upgrade google-cloud-texttospeech

#dialogflow
pip install dialogflow
 
#play 
pip install python-vlc
