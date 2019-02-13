#!/bin/bash
echo 'start running test06_rejectchemistrywitness_jane automation'
python -m pytest testcases\ELN_test\test06_rejectchemistrywitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport