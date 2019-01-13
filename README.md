###Prerequisites
Follow this link to install Allure
https://docs.qameta.io/allure/#_installing_a_commandline

###Setup
1) Install python3 and pip3 if not installed.
2) Install the following packages if not installed.
    1. pip install selenium
    2. pip install webdriver-manager
    3. pip install pytest
    4. pip install allure-pytest

### Generate Report 
python login_test_admin.py --alluredir loginreport

###Start Allure server to view report
allure serve loginreport