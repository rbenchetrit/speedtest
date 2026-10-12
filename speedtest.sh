#!/bin/bash
date >> /home/pi/src/speedtest/speedtest.log
python /home/pi/src/speedtest/speedtest.py >> /home/pi/src/speedtest/speedtest.log
