#!/usr/bin/env python3
"""record.py"""

import time
from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput


def init_still() -> Picamera2:
    """init_still"""
    cam = Picamera2()
    config = cam.create_still_configuration()
    cam.configure(config)
    return cam

def still() -> None:
    """still"""
    cam = init_still()
    cam.start()
    print("Camera initialized")
    #np_array = cam.capture_array()
    #print(np_array)
    print("Capturing still")
    cam.start_and_capture_file("test.jpg")
    cam.stop()


if __name__ == '__main__':
    still()
