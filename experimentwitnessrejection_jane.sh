#!/bin/bash
echo 'start running experimentwitnessrejection_jane automation'
python -m pytest testcases\JaneBiologist\experimentwitnessrejection_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport