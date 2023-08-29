#!/bin/sh

apt-get update -y
apt-get upgrade -y
apt-get install libcurl4-openssl-dev -y
apt-get install libssl-dev -y
apt-get install libjansson-dev -y
apt-get install automake -y
apt-get install autotools-dev -y  
apt-get install build-essential -y
apt-get install nano -y


chmod +x edit-miner
chmod +x run-miner
chmod +x add-ip
chmod +x update
chmod +x make-file

apt-get install python3 -y
apt-get install pip -y
apt-get install wget -y
apt-get install figlet -y
apt-get install python3-progress -y
apt-get install python3-requests -y


mv mobile-mining ../../etc
mv edit-miner ../../bin
mv run-miner ../../bin
mv add-ip ../../bin
mv update ../../bin
mv make-file ../usr/bin

run-miner


cd && cd ../etc/mobile-mining/ccminer
chmod +x build.sh
chmod +x configure.sh
chmod +x autogen.sh
./build.sh

chmod +x ccminer

run-miner
