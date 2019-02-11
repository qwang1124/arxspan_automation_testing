#!/bin/bash
echo 'start running analyticalacceptrejectedwitness_jane automation'
python -m pytest testcases\JaneBiologist\analyticalacceptrejectedwitness_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport