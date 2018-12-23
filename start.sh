#!/bin/sh
export PYTHONPATH='/home/pi/git/pi-robot/'
#export PAFY_BACKEND=internal
cd /home/pi/git/pi-robot/

echo *Starting STT service*
python microService/speachToTextService.py &

echo *Starting TTS Serivce*
python microService/hebTextToSpeachService.py &

echo *Starting AI Service*
python microService/dialogFlowService.py &

echo *Starting Translation Service*
python microService/translateService.py &

echo *Starting Record Serivce*
python microService/recordVoiceService.py &

tail -f logs/*
