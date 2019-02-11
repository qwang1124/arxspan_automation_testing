#!/bin/bash
echo 'start running experiment_jane automation'
python -m pytest testcases\JaneBiologist\experiment_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport