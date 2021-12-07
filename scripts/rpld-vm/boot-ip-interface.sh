#!/usr/bin/bash
sudo ip link set enp0s3 up
sudo dhclient enp0s3
sudo ip link set enp0s9 up