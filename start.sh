#!/bin/sh
export PYTHONPATH='/home/pi/git/pi-robot/'
#export PAFY_BACKEND=internal
echo  *Starting spotify Client
systemctl --user start spotifyd.service

cd /home/pi/git/pi-robot/

echo *Starting STT service*
python microService/speachToTextService.py &

echo *Starting TTS Serivce*
python microService/hebTextToSpeachService.py &

echo *Starting AI Service*
python microService/dialogFlowService.py &

echo *Starting Translation Service*
python microService/translateService.py &

echo *Starting Action Serivce*
python microService/actionService.py &

echo *Starting Record Serivce*
python microService/recordVoiceService.py &

echo *Start Flask API
python3 microService/apiService.py &

echo *Start Web port 3000
yarn start

tail -f logs/*

