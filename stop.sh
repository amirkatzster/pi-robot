#!/bin/bash

pkill -f python
#pkill -9 $(ps aux | grep react | awk '{print $2}')
kill -9 `ps aux | grep react | grep -v grep | awk '{print $2}'`

