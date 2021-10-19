#!/bin/bash

# You may need to run this script iwth elevated priviledges (sudo)
echo "export CASDROP_WATCH_FOLDER='<drop_folder>'" >> ~/.bashrc
echo "export CASDROP_SERVER_URL='<file_server_url>'" >> ~/.bashrc
echo "export CASDROP_SPKR_NAME='<your_chromecast_speaker_friendly_name>'" >> ~/.bashrc
echo "export CASDROP_TV_NAME='<your_chromecast_television_friendly_name>'" >> ~/.bashrc


source ~/.bashrc