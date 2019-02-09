#!/bin/bash
echo 'start running analyticalwitness_joe automation'
python -m pytest testcases/JoeChemist/analyticalwitness_joe.py --alluredir JoeChemist
echo 'start generating the report'
allure serve JoeChemist