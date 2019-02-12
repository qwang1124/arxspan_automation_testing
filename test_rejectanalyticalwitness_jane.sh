#!/bin/bash
echo 'start running test_rejectanalyticalwitness_jane automation'
python -m pytest testcases\test_JaneBiologist\test_rejectanalyticalwitness_jane.py --alluredir test_JaneBiologist
echo 'start generating the report'
allure serve test_JaneBiologist