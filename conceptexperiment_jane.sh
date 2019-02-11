#!/bin/bash
echo 'start running conceptexperiment automation'
python -m pytest testcases\JaneBiologist\conceptexperiment_jane.py --alluredir JaneBiologistreport
echo 'start generating the report'
allure serve JaneBiologistreport