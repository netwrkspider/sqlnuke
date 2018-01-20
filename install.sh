#!/bin/bash

mkdir /root/bin/
cd /root/bin
apt get update
apt install tor
apt install sqlmap
git clone https://github.com/netwrkspider/sqlnuke.git
echo "UPDATE YOUR TELEGRAM BOT TOKEN on config.py file"
