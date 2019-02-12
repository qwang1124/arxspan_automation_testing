#!/bin/bash
echo 'start running test_conceptexperiment automation'
python -m pytest testcases\test_JaneBiologist\test_conceptexperiment_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport