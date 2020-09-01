#!/usr/bin/env python

import signal
import sys


def signal_handler(signal, frame):
    sys.exit(0)


signal.signal(signal.SIGINT, signal_handler)


def main():
    while True:
        x = input("What's up?\n")


main()
