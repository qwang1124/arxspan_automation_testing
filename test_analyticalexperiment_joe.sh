#!/bin/bash
echo 'start running test_analyticalexperiment_joe automation'
python -m pytest testcases/test_JoeChemist/test_analyticalexperiment_joe.py --alluredir test_JoeChemist
echo 'start generating the report'
allure serve test_JoeChemistJoeChemist