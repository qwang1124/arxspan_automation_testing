#!/bin/bash
echo 'start running test_chemistryexperiment_joe automation'
python -m pytest testcases/test_JoeChemist/test_chemistryexperiment_joe.py --alluredir test_JoeChemist
echo 'start generating the report'
allure serve test_JoeChemist