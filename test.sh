#!/bin/sh

cd /home/pi/git/pi-robot/
python -m unittest discover -v -s tests
