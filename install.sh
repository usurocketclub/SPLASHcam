#!/bin/bash

mkdir installer
cd installer

wget -O install_pivariety_pkgs.sh https://github.com/ArduCAM/Arducam-Pivariety-V4L2-Driver/releases/download/install_script/install_pivariety_pkgs.sh
chmod +x install_pivariety_pkgs.sh

sudo apt update
./install_pivariety_pkgs.sh -p libcamera_dev
./install_pivariety_pkgs.sh -p libcamera_apps
./install_pivariety_pkgs.sh -p imx519_kernel_driver_low_speed
#./install_pivariety_pkgs.sh -p 64mp_pi_hawk_eye_kernel_driver

#sudo apt install -y python3-opencv
#sudo apt install -y opencv-data

#pip3 install tflite-runtime

echo
echo "!!!!!!!!!!!!!!!!!!!!!"
echo "!! reboot required !!"
echo "!!!!!!!!!!!!!!!!!!!!!"

