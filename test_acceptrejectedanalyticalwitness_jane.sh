#!/bin/bash
echo 'start running test_acceptrejectedanalyticalwitness_jane automation'
python -m pytest testcases\test_JaneBiologist\test_acceptrejectedanalyticalwitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport