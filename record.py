#!/usr/bin/env python3
"""record.py"""

import signal
import sys
import subprocess
import RPi.GPIO as GPIO


INTERRUPT_PIN = 4

TIMELAPSE_COMMAND="libcamera-still -t 60000 --timelapse 1 -o experiment%04d.jpeg"
VIDEO_COMMAND="libcamera-vid --mode 1920:1080 --width 640 --height 480 --framerate 120 --codec h264 --bitrate 50000000 --intra 1 --vflip --hflip --autofocus-mode manual --lens-position 5 -o experiment.h264 -t 60000 -n"


def signal_handler():
    """signal_handler"""
    GPIO.cleanup()
    sys.exit(0)


def interrupt_callback(channel):
    """interrupt_callback"""
    if GPIO.input(INTERRUPT_PIN):
        print("recording started")
        #rval = subprocess.call(TIMELAPSE_COMMAND.split())
        rval = subprocess.call(VIDEO_COMMAND.split())
        print("timelapse complete")
        print("exiting")


if __name__ == '__main__':
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(INTERRUPT_PIN, GPIO.IN)
    GPIO.add_event_detect(INTERRUPT_PIN, GPIO.RISING, callback=interrupt_callback)
    print("GPIO callback registered")
    signal.signal(signal.SIGINT, signal_handler)
    signal.pause()
    GPIO.cleanup()
