import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessrejectionjane')
    def test1(self):
        driver = testjanelogin()
        self.assertIn('CX Upgrade (Reg) TS Firefox - 001', driver.find_element_by_class_name('experimentCell').text)
        driver.find_element_by_class_name('experimentCell').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(2)')
        button.click()
        driver.find_element_by_id('reasonBox').send_keys('TESTING')

        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

