#!/bin/bash
echo 'start running test03_acceptnotebookshare_jane automation'
python -m pytest testcases\ELN_test\test03_acceptnotebookshare_jane.py --alluredir test_JaneBiologistreport
echo 'start generating the report'
allure serve test_JaneBiologistreport