#!/bin/bash
echo 'start running login automation'
python -m pytest testcases\conceptexperiment\analyticalexperiment_joe.py --alluredir conceptexperimentreport
echo 'start generating the report'
allure serve conceptexperimentreport