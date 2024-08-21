#Installing Python

echo Installing Python Version:3.8...
sudo apt-get install software-properties-common
sudo add-apt-repository ppa:deadsnake/ppa
sudo apt-get update
sudo apt-get install python3.8

#Installing PyQt5

echo Installing PyQt5...
sudo apt update && sudo apt install python3-pip
pip3 install PyQt5
sudo apt install qtcreator pyqt5-dev-tools

#Updating (Again) and upgrading

echo 
echo 
echo Finishing installation
echo
echo
echo - - - - - - - - - - - - - - - - - - - - - - - - -


sudo apt update && sudo apt upgrade

echo 
echo 
echo Instalation finished!
