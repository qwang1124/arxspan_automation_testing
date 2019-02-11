#!/bin/bash
echo 'start running JaneBiologist automation'
python -m pytest testcases/experiment/experiment_joe.py --alluredir experimentreport
echo 'start generating the report'
allure serve experimentreport