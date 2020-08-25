#! /usr/bin/env python3
# countdown.py - A simple countdown script

import time
import subprocess

time_left = 10
while time_left > 0:
    print(time_left, end="")
    time.sleep(1)
    time_left = time_left - 1

# At the end of the countdown, play a sound file.
subprocess.Popen(["see", "/home/comet/bin/automate_online-materials/alarm.wav"])
