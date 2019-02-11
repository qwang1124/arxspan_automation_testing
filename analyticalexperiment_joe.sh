#!/bin/bash
echo 'start running analyticalexperiment_joe automation'
python -m pytest testcases/JoeChemist/analyticalexperiment_joe.py --alluredir JoeChemist
echo 'start generating the report'
allure serve JoeChemist