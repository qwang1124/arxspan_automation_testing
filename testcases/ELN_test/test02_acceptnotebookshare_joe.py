# Test ID: testELN-02
# Test name: Joe has accept the note book share by Admin Test
# Expect output:
#      1. Check received invitation from Admin ;
#      2. Successful accept the note book share request send by Admin;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Click on the invitation;
#      5. Select the note book name which shared by Admin;
#      6. Accept the share notification.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import unittest, time, re, os
import allure


class TestNotebookJoe(unittest.TestCase):
    @allure.testcase('test Admin share acceptation')
    def test1(self):
        driver = joelogin()
        driver.find_element_by_link_text('Invitations').click()
        time.sleep(2)
        driver.find_element_by_css_selector('#SummaryTable > tbody > tr > td.sorting_1 > a').click()
        time.sleep(2)
        # accept the note book share
        driver.switch_to.window(driver.window_handles[1])
        # assert driver.find_element_by_xpath('//*[@id="acceptForm"]/input[3]').is_displayed()
        driver.find_element_by_css_selector('#acceptForm > input:nth-child(3)').click()
        driver.close()


def joelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
