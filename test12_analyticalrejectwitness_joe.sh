#!/bin/bash
echo 'start running test12_analyticalrejectwitness_joe automation'
python -m pytest testcases/ELN_test/test12_analyticalrejectwitness_joe.py --alluredir test_JoeChemistreport
echo 'start generating the report'
allure serve test_JoeChemistreport