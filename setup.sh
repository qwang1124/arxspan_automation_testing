#!/bin/bash
echo "install pip3"
sudo apt-get install python3-pip
echo "install selenium"
pip3 install selenium
echo "install webdriver-manager"
pip3 install webdriver-manager
echo "install install pytest"
pip3 install pytest
echo "install allure pytest"
pip3 install allure-pytest
echo "running test case"
./test01_notebook_admin.sh