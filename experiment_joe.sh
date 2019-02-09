#!/bin/bash
echo 'start running experiment_joe automation'
python -m pytest testcases/JoeChemist/experiment_joe.py --alluredir JoeChemist
echo 'start generating the report'
allure serve JoeChemist