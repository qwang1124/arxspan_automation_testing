#!/bin/bash
echo 'start running experimentwitnessrejectedacceptation_jane automation'
python -m pytest testcases\JaneBiologist\experimentwitnessrejectedacceptation_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport