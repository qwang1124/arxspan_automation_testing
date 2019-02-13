#!/bin/bash
echo 'start running test_acceptnotebookshare_jane automation'
python -m pytest testcases\ELN_test\test02_acceptnotebookshare_joe.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport