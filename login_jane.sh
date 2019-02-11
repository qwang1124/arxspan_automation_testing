#!/bin/bash
echo 'start running login_test_Jane automation'
python -m pytest testcases/login/login_test_Jane.py --alluredir loginreport
echo 'start generating the report'
allure serve loginreport