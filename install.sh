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
echo "Recompiling libcamera-app to add support for Pi Zero"
echo

sudo apt install -y libcamera-dev libjpeg-dev libtiff5-dev
sudo apt install libavcodec-dev libavdevice-dev libavformat-dev libswresample-dev # ffmpeg encoding
sudo apt install -y cmake libboost-program-options-dev libdrm-dev libexif-dev

git clone https://github.com/raspberrypi/libcamera-apps.git
cd libcamera-apps
mkdir build
cd build
cmake .. -DENABLE_DRM=0 -DENABLE_X11=0 -DENABLE_QT=0 -DENABLE_OPENCV=0 -DENABLE_TFLITE=0
make -j1  # use -j1 on Raspberry Pi 3 or earlier devices
sudo make install
sudo ldconfig # this is only necessary on the first build

echo
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
echo "!! reboot may be required !!"
echo "!!!!!!!!!!!!!!!!!!!!!!!!!!!!"

