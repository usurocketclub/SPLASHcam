#!/usr/bin/env python3
"""example.py"""

import time
from picamera2.encoders import H264Encoder
from picamera2.outputs import CircularOutput
from picamera2 import Picamera2


picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration())

encoder = H264Encoder()
output = CircularOutput()

picam2.start_recording(encoder, output)

output.fileoutput = "example.h264"

time.sleep(5)
output.start()

time.sleep(5)
picam2.stop_recording()
