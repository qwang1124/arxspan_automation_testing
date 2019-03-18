from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os


class TestNotebookJoe(unittest.TestCase):

    def test_sharenotebook(self):
        driver = joelogin()
        driver.find_element_by_link_text('Invitations').click()
        driver.get('https://model.arxspan.com//arxlab//show-notebooks.asp?id=10669')
        time.sleep(3)
        driver.find_element_by_xpath("//input[@type='button' and @value='Accept']").click()
        # driver.find_element_by_css_selector("input[onlick=notebookAccept()]").click()
        driver.close()


def joelogin():
    driver = webdriver.Chrome('C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\Driver\\chromedriver.exe')
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


listaa = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\ArxspanAutomationTest'


def createsuite1():
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='NotebookShare_test_Joe.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


currenttime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
reportfile = 'ResultReport' + currenttime + '.html'
filename = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports\\result.html'
fp = open(filename, 'wb')
filepath = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports'

runner = HTMLTestRunner(output=filepath)

runner.run(createsuite1())

fp.close()

