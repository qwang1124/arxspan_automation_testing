#!/bin/bash
echo 'start running login_test_Joe automation'
python -m pytest testcases/login/login_test_Joe.py --alluredir loginreport
echo 'start generating the report'
allure serve loginreport