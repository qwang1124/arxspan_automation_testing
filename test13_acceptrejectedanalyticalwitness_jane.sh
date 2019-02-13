#!/bin/bash
echo 'start running test13_acceptrejectedanalyticalwitness_jane automation'
python -m pytest testcases\ELN_test\test13_acceptrejectedanalyticalwitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport