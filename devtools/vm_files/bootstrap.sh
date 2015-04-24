#!/usr/bin/env bash

VAGRANT_HOME=/home/vagrant

# Turn off interactive mode
export DEBIAN_FRONTEND=noninteractive

echo -e "\n\n\t\t===> Updating packages <===\n\n"

#apt-get update

echo -e "\n\n\t\t===> Installing pip <===\n\n"
sudo apt-get install -y python3-pip

echo -e "\n\n\t\t===> Installing virtualenvwrapper <===\n\n"
sudo pip3 install virtualenvwrapper
rm -R $VAGRANT_HOME/.virtualenvs
mkdir $VAGRANT_HOME/.virtualenvs
export WORKON_HOME=$VAGRANT_HOME/.virtualenvs
echo "VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'" >> $VAGRANT_HOME/.profile
echo "source /usr/local/bin/virtualenvwrapper.sh" >> $VAGRANT_HOME/.profile

VIRTUALENVWRAPPER_PYTHON='/usr/bin/python3'
source /usr/local/bin/virtualenvwrapper.sh

sudo chown -R vagrant:vagrant $VAGRANT_HOME/.virtualenvs
