#!/bin/bash
date >> /home/pi/src/speedtest/speedtest.log
python /home/pi/src/speedtest/speedtest.py >> /home/pi/src/speedtest/speedtest.log
#gdrive sync upload /home/pi/src/speedtest/speedtest.csv 1VQlhmOdhdsBeIf5Mab4u_lV5A1zjZAA_ >> /home/pi/src/speedtest/speedtest.log
