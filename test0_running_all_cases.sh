#!/bin/bash
echo 'start running test_ELN_all_cases automation'
python -m pytest testcases/ELN_test/test01_notebook_all_admin.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test02_acceptnotebookshare_joe.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test03_acceptnotebookshare_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test04_chemistryexperiment_all_joe.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test05_biologyexperiment_all_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test06_rejectchemistrywitness_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test07_chemistryrejectwitness_all_joe.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test08_acceptrejectedchemistrywitness_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test09_analyticalexperiment_all_joe.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test10_conceptexperiment_all_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test11_rejectanalyticalwitness_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test12_analyticalrejectwitness_joe.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test13_acceptrejectedanalyticalwitness_jane.py --alluredir test_ELN_report
echo 'start generating the report'
allure serve test_ELN_report
