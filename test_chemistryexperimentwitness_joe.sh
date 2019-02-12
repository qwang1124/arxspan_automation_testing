#!/bin/bash
echo 'start running test_chemistryexperimentwitness_joe automation'
python -m pytest testcases/test_JoeChemist/test_chemistryexperimentwitness_joe.py --alluredir test_JoeChemist
echo 'start generating the report'
allure serve test_JoeChemist