from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestNotebookJoe(unittest.TestCase):
    @allure.testcase('test share test_admin acceptation')
    def test1(self):
        driver = janelogin()
        driver.find_element_by_link_text('Invitations').click()
        driver.find_element_by_css_selector('#SummaryTable > tbody > tr.odd > td:nth-child(1) > a').click()
        time.sleep(2)
        driver.switch_to_window(driver.window_handles[1])

        # assert driver.find_element_by_xpath('//*[@id="acceptForm"]/input[3]').is_displayed()
        driver.find_element_by_css_selector('#acceptForm > input:nth-child(3)').click()
        driver.close()


def janelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/test_login.asp')
    driver.maximize_window()
    driver.find_element_by_id('test_login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    return driver
