#!/usr/bin/env python3

from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
import time


def initStill() -> Picamera2:
    cam = Picamera2()
    config = cam.create_still_configuration()
    cam.configure(config)
    return cam

def still() -> None:
    cam = initStill()
    cam.start()
    print("Camera initialized")
    #np_array = cam.capture_array()
    #print(np_array)
    print("Capturing still")
    cam.start_and_capture_file("test.jpg")
    cam.stop()


def initRecord() -> Picamera2:
    cam = Picamera2()
    config = cam.create_video_configuration()
    cam.configure(config)
    cam.resolution = (640, 480)
    cam.framerate = 32
    return cam

def record() -> None:
    cam = initRecord()
    encoder = H264Encoder(10000000)
    output  = FfmpegOutput("test.mp4")
    cam.start_recording(encoder, output)
    time.sleep(5)
    cam.stop_recording()


if __name__ == '__main__':
    record()

