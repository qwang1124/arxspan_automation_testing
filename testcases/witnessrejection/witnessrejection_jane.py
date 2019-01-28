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
        assert driver.find_element_by_id('witnessRequestsHolder').is_displayed()
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(2)')
        button.click()
        driver.find_element_by_id('reasonBox').send_keys('TESTING')
        driver.find_element_by_id('rejectSubmitButton').click()
        time.sleep(1)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
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

