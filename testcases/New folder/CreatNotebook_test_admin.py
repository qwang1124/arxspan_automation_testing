from HtmlTestRunner import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
import time
import re
import os
import HtmlTestRunner


class TestCreatenotebookAdmin(unittest.TestCase):

    def testcreatenotebook(self):
        driver = testadminlogin()

        # create notebooks by admin start
        driver.find_element_by_id('createNewNotebookLeftNavButton').click()
        driver.find_element_by_id('notebookName').send_keys('Test_Notebook_Q')
        driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
        driver.find_element_by_name('createNotebook').click()

    def testsharenotebook(self):
        driver = testadminlogin()
        driver.get('https://model.arxspan.com//arxlab//show-notebooks.asp?id=10733')

        # Share notebooks with Joe Chemistry
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('expandGroupLink-104').click()
        driver.find_element_by_id('listGroupCheckUser-936').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Select']").click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Share']").click()

        # Share notebooks with Jane Biology
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('expandGroupLink-105').click()
        driver.find_element_by_id('listGroupCheckUser-937').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Select']").click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Share']").click()

        driver.find_element_by_link_text('Logout').click()




        # test_value = driver.find_element_by_id('NotebookTitle').text
        # print(test_value)
        # a = 'Test_Notebook_QingWang'
        # test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        # b = 'System Administrator'
        # test_value3 =driver.find_element_by_id('notebookDescription').text
        # print(test_value2)
        # c = 'Test Script execution-01/01/2019'
        #
        # if a in test_value and b in test_value2 and c in test_value3:
        #     valid = True
        # else:
        #     valid = False
        #     picture_name = 'test_CreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
        #     driver.get_screenshot_as_file(picture_name)
        # self.assertTrue(valid)

        # Logout
        driver.find_element_by_link_text('Logout').click()


def testadminlogin():
    driver = webdriver.Chrome('..\\chromedriver.exe')
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('admin@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


listaa = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\ArxspanAutomationTest\\notebook_test'


def createsuite1():
    testunit=unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(listaa, pattern='CreatNotebook_test_admin.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit


if __name__ == '__main__':
    currenttime = time.strftime("%Y-%m-%d %H_%M_%S", time.localtime(time.time()))
    reportfile = 'ResultReport' + currenttime + '.html'
    filename = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports\\result.html'
    fp = open(filename, 'wb')
    filepath = 'C:\\Users\\QingW\\PycharmProjects\\FirstSeleium\\reports'

    runner = HTMLTestRunner(output=filepath)

    runner.run(createsuite1())

    fp.close()

