# Test ID: testELN-03
# Test name: Jane has accept the note book share by Admin Test
# Expect output:
#      1. Check received invitation from Admin ;
#      2. Successful accept the note book share request send by Admin;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Click on the invitation;
#      5. Select the note book name which shared by Admin;
#      6. Accept the share notification.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestNotebookJane(unittest.TestCase):
    @allure.testcase('test share test_admin acceptation')
    def test1(self):
        driver = janelogin()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text('Invitations').click()
        driver.find_element_by_xpath('//*[@id="SummaryTable"]/tbody/tr/td[1]/a').click()
        # accept the note book share
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_css_selector('#acceptForm > input:nth-child(3)').click()
        driver.close()


def janelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    # driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
