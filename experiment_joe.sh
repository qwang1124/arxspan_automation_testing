#!/bin/bash
<<<<<<< HEAD
echo 'start running JaneBiologist automation'
python -m pytest testcases/experiment/experiment_joe.py --alluredir experimentreport
=======
echo 'start running experiment_joe automation'
python -m pytest testcases/JoeChemist/experiment_joe.py --alluredir JoeChemist
>>>>>>> c5e124cb3fe2cfceb7c3556c67722874ba0535ed
echo 'start generating the report'
allure serve JoeChemist