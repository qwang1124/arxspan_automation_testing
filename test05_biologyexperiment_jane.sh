#!/bin/bash
echo 'start running test_biologyexperiment_jane automation'
python -m pytest testcases\ELN_test\test05_biologyexperiment_all_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport