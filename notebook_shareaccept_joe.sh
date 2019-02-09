#!/bin/bash
echo 'start running notebook_shareaccept_joe automation'
python -m pytest testcases/JoeChemist/notebook_shareaccept_joe.py --alluredir JoeChemist
echo 'start generating the report'
allure serve JoeChemist