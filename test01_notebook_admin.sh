#!/bin/bash
echo 'start running test01_notebook_all_admin automation'
python -m pytest testcases/ELN_test/test01_notebook_all_admin.py --alluredir test_Adminreport
echo 'start generating the report'
allure serve test_Adminreport