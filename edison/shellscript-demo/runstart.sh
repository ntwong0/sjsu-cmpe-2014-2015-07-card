#!/bin/bash

cd /home/card/edison/shellscript-demo
sh setupSerial.sh
cd /home/card/webgui
node server.js &
cd /home/card/slam/engine
python engine.py &