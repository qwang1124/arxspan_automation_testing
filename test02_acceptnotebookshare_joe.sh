#!/bin/bash
echo 'start running test02_acceptnotebookshare_joe automation'
python -m pytest testcases/ELN_test/test02_acceptnotebookshare_joe.py --alluredir test_JoeChemistreport
echo 'start generating the report'
allure serve test_JoeChemistreport