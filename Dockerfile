FROM python:3

ADD . /

RUN pip install gTTS
RUN pip install urllib3
RUN pip install pydub
RUN pip install pyaudio
#stt
RUN pip install --upgrade google-cloud-speech
ENV GOOGLE_APPLICATION_CREDENTIALS="$((Get-Item -Path ".\").FullName)\Hidden\robot-pi-d6c05e651bc4.json"
#translate
RUN pip install --upgrade google-cloud-translate
#tts
RUN pip install --upgrade google-cloud-texttospeech
#dialogflow
RUN pip install dialogflow
#play 
RUN pip install python-vlc

CMD [ "python", "./robot.py" ]
