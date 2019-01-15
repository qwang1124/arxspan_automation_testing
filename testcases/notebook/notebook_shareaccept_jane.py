from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestNotebookJoe(unittest.TestCase):
    @allure.testcase('test share notebook acceptation')
    def test1(self):
        driver = janelogin()
        driver.find_element_by_link_text('Invitations').click()
        driver.get('https://model.arxspan.com/arxlab/show-notebook.asp?id=10752')
        time.sleep(3)
        assert(driver.find_element_by_xpath("//input[@type='button' and @value='Accept']").is_displayed())


def janelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
