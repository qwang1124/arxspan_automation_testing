#!/bin/bash
echo 'start running test_ELN_all_cases automation'
#python -m pytest testcases/ELN_test/test01_notebook_all_admin.py --alluredir test_ELN_report
#python -m pytest testcases/ELN_test/test02_acceptnotebookshare_joe.py --alluredir test_ELN_report
#python -m pytest testcases/ELN_test/test03_acceptnotebookshare_jane.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test04_chemistryexperiment_all_joe_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test05_rejectchemistrywitness_jane_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test06_chemistryrejectwitness_all_joe_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test07_acceptrejectedchemistrywitness_jane_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test08_analyticalexperiment_all_joe_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test09_rejectanalyticalwitness_jane_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test10_analyticalrejectwitness_joe_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test11_acceptrejectedanalyticalwitness_jane_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test12_biologyexperiment_all_jane_test.py --alluredir test_ELN_report
python -m pytest testcases/ELN_test/test13_conceptexperiment_all_jane_test.py --alluredir test_ELN_report
echo 'start generating the report'
allure serve test_ELN_report