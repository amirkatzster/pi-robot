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

#rabbitMq 
pip install pika
apt-get install –y erlang logrotate
apt-get -f install
#wget https://github.com/rabbitmq/rabbitmq-server/releases/download/v3.7.9/rabbitmq-server_3.7.9-1_all.deb
#dpkg -i rabbitmq-server_3.7.9-1_all.deb
wget https://www.rabbitmq.com/releases/rabbitmq-server/v3.6.3/rabbitmq-server_3.6.3-1_all.deb
dpkg -i rabbitmq-server_3.6.3-1_all.deb
sudo rabbitmq-plugins enable rabbitmq_management
sudo rabbitmqctl add_user rabbituser 123456
sudo rabbitmqctl set_user_tags  rabbituser administrator
sudo rabbitmqctl set_permissions -p / rabbituser ".*" ".*" ".*"
