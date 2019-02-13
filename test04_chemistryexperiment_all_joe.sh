#!/bin/bash
echo 'start running test04_chemistryexperiment_all_joe automation'
python -m pytest testcases/Eln_test/test04_chemistryexperiment_all_joe.py --alluredir test_JoeChemistreport
echo 'start generating the report'
allure serve test_JoeChemistreport