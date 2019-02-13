#!/bin/bash
echo 'start running test08_acceptrejectedchemistrywitness_jane automation'
python -m pytest testcases\ELN_test\test08_acceptrejectedchemistrywitness_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport