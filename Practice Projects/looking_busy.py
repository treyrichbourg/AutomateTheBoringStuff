#! /usr/bin/env python3
# looking_busy.py - This script will nudge the mouse slightly every 10 seconds to keep IM status from going afk.

import pyautogui as pyag
import time
import sys


def look_busy(time):
    pyag.PAUSE = time
    while True:
        pyag.move(2, 0)
        pyag.move(-2, 0)


def main():
    if len(sys.argv) >= 2:
        time = int(sys.argv[1])
        look_busy(time)
    else:
        print("Please enter time frequency as an argument")


if __name__ == "__main__":
    main()
