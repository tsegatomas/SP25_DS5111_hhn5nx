#!/bin/bash

# Download Chrome
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb

# Install Chrome
sudo apt install -y ./google-chrome-stable_current_amd64.deb

# Cleanup
rm google-chrome-stable_current_amd64.deb
