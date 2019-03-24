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

echo *Starting Camera Web Service
#python3 microService/camera_web_service.py &
raspistill -w 640 -h 480 -q 5 -o resources/stream/pic.jpg -tl 100 -t 9999999 -th 0:0:0 > /dev/null 2>&1 &
LD_LIBRARY_PATH=/usr/local/lib mjpg_streamer -i "input_file.so -f resources/stream -n pic.jpg" -o "output_http.so -w /usr/local/www -p 8081" &

echo *Start Web port 3000

cd web-app
yarn start &
cd ..

tail -f logs/*

