#!/bin/bash
echo 'start running login_test_admin automation'
python -m pytest testcases/login/login_test_admin.py --alluredir loginreport
echo 'start generating the report'
allure serve loginreport

