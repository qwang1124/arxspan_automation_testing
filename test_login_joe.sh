#!/bin/bash
echo 'start running login_test_Joe automation'
python -m pytest testcases/test_login/login_test_Joe.py --alluredir test_loginreport
echo 'start generating the report'
allure serve test_loginreport