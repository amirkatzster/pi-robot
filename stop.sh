#!/bin/bash

sudo pkill -f python
sudo pkill -f python3
sudo pkill -f raspistill
sudo pkill -f mjpg_streamer
kill -9 `ps aux | grep python | grep -v grep |awk '{print $2}'`
kill -9 `ps aux | grep react | grep -v grep | awk '{print $2}'`

