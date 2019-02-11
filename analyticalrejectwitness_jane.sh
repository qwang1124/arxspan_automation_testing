#!/bin/bash
echo 'start running analyticalrejectwitness_jane automation'
python -m pytest testcases\JaneBiologist\analyticalrejectwitness_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport