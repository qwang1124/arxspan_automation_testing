#!/bin/bash
echo 'start running test10_conceptexperiment_all_jane automation'
python -m pytest testcases\ELN_test\test10_conceptexperiment_all_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport