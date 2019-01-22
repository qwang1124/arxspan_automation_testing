import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessrejectionjoe')
    def test1(self):
        driver = testjoelogin()
        self.assertIn('Rejection', driver.find_element_by_class_name('notificationBodyTitle').text)
        driver.find_element_by_class_name('experimentCell').click()
        button = driver.find_element_by_css_selector('#pageContentTD > div > a')
        button.click()

        driver.get('https://model.arxspan.com/arxlab/misc/show-notifications.asp')
        driver.find_element_by_css_selector('#notification_body_153636 > span.noteText > p:nth-child(1) > a').click()
        driver.find_element_by_id('noteTable_tab').click()
        driver.find_element_by_css_selector('#note_68255_tr > td:nth-child(1) > a').click()
        self.assertIn('TESTING', driver.find_element_by_id('note_68255_description').text)
        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        # witness failed because experiment need review
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()

        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjoelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

