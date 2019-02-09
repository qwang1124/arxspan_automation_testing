#!/bin/bash
echo 'start running notebook_shareaccept_jane automation'
python -m pytest testcases\JaneBiologist\notebook_shareaccept_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport