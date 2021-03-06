#!/bin/bash
echo "install pip3"
sudo apt-get install python3-pip
echo "install selenium"
pip3 install selenium
echo "install webdriver-manager"
pip3 install webdriver-manager
echo "install install pytest"
pip3 install pytest
pip install pytest-cov 
pip install pytest-xdist 
pip install pytest-bdd 
echo "install allure pytest"
pip3 install allure-pytest
# echo "install allure"
# sudo apt-add-repository ppa:qameta/allure
# sudo apt-get update 
# sudo apt-get install allure
