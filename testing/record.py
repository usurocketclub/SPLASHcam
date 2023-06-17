#!/usr/bin/env python3

from picamera2.encoders import H264Encoder
from picamera2 import Picamera2
import time


cam = Picamera2()
cam.video_configuration.main.size = (1920, 1080)
#cam.video_configuration.main.size = (640, 480)
cam.video_configuration.controls.FrameRate = 30
cam.configure('video')

encoder = H264Encoder(60*1000*1000)
output = "test.h264"

cam.start_recording(encoder, output)
time.sleep(10)
cam.stop_recording()

