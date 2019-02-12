#!/bin/bash
echo 'start running test_notebook_admin automation'
python -m pytest testcases/test_Admin/test_notebook_admin.py --alluredir test_Admin
echo 'start generating the report'
allure serve test_Admin