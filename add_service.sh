#!/bin/bash

sudo ln -sf /home/pi/splash/splashcam.service /etc/systemd/system/splashcam.service

sudo systemctl daemon-reload
sudo systemctl enable splashcam
sudo systemctl start splashcam
