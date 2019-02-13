#!/bin/bash
echo 'start running test09_analyticalexperiment_all_joe automation'
python -m pytest testcases/ELN_test/test09_analyticalexperiment_all_joe.py --alluredir test_JoeChemistreport
echo 'start generating the report'
allure serve test_JoeChemistJoeChemistreport