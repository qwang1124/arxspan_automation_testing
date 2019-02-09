#!/bin/bash
echo 'start running experimentwitness_joe automation'
python -m pytest testcases/JoeChemist/experimentwitness_joe.py --alluredir JoeChemist
echo 'start generating the report'
allure serve JoeChemist