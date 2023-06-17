#!/bin/bash

libcamera-vid --mode 1920:1080 --width 640 --height 480 --framerate 120 --codec h264 --bitrate 50000000 --intra 1 -o test.h264 -t 20000 -n
