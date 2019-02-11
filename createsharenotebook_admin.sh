#!/bin/bash
echo 'start running createsharenotebook_admin automation'
python -m pytest testcases/Admin/createsharenotebook_admin.py --alluredir Admin
echo 'start generating the report'
allure serve Admin