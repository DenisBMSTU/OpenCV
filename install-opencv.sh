#!/bin/bash

###########################################################
#
# Opencv-2.4.11
# http://opencv.org/
#
###########################################################

sudo apt-get update
sudo apt-get upgrade

sudo apt-get -y install libopencv-dev build-essential cmake git libgtk2.0-dev pkg-config python-dev python-numpy libdc1394-22 libdc1394-22-dev libjpeg-dev libpng12-dev libtiff4-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev libtbb-dev libqt4-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils unzip
 
FOLDER_NAME="opencv"
 
mkdir ${FOLDER_NAME}
 
cd ${FOLDER_NAME}
 
wget https://github.com/DenisBMSTU/install_opencv/archive/master.zip -O opencv-2.4.11.zip

unzip opencv-2.4.11.zip
 
cd install_opencv-master
 
mkdir build

cd build

cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D WITH_V4L=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
 
make -j $(nproc)
 
sudo make install
 
sudo /bin/bash -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
 
sudo ldconfig
 

