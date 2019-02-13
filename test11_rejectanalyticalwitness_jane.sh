#!/bin/bash
echo 'start running test11_rejectanalyticalwitness_jane automation'
python -m pytest testcases\ELN_test\test11_rejectanalyticalwitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport