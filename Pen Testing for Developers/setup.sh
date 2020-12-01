#!/bin/bash
:<<'COMMENT'
Author: Chris Duffy
Date: 2015
Name: setup.sh
Purpose: This installation file does the basic installation of PIP, and relevant Python libraries.
Systems: This has only been tested on Kali
COMMENT

# Installing PIP
#apt-get clean && apt-get update && apt-get upgrade -y && apt-get dist-upgrade -y # Uncomment if necessary
apt-get -y install python-setuptools python-dev python-pip

# Install Python libraries
pip install netifaces python-nmap scapy msgpack-python twill xlsxwriter
# Upgrade requests
pip install request --upgrade

# Clone MSFRPC
cd /opt
git clone https://github.com/SpiderLabs/msfrpc.git

# Install Perl interface for MSFRPC
cd /opt/msfrpc/Net-MSFRPC
perl Makefile.PL
make
make install

# Install Python interface for MSFRPC
cd /opt/msfrpc/python-msfrpc
python ./setup.py build
python ./setup.py install