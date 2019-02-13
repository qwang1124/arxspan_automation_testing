#!/bin/bash
echo 'start running test_analyticalwitness_joe automation'
python -m pytest testcases/test_JoeChemist/test_analyticalwitness_joe.py --alluredir test_JoeChemistreport
echo 'start generating the report'
allure serve test_JoeChemistreport