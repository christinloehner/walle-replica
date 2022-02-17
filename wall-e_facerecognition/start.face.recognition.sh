#!/bin/bash
workdir="/home/pi/facial_recognition"
cd ${workdir}
sudo /usr/bin/python3 ./walle-face-req.py >/dev/null 2>&1 &

