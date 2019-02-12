#!/bin/bash
echo 'start running test_rejectchemistrywitness_jane automation'
python -m pytest testcases\test_JaneBiologist\test_rejectchemistrywitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport