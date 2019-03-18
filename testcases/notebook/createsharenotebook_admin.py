import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import platform
import json
from pathlib import Path


class TestCreatenotebookAdmin(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        if platform.system() == 'Windows':
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif platform.system() == "Darwin":
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"

        self.verificationErrors = []
        self.accept_next_alert = True

    # def test_create_chemistryexperiment(self):
    #     driver = self.driver
    #     driver.get(self.base_url)
    #     driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    #     driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    #     driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    #     select = Select(driver.find_element_by_tag_name('select'))
    #     select.select_by_visible_text('Model Test Script Company')
    #     driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    #     cookies = driver.get_cookies()
    #     print(type(cookies))
    #     # print ("".join(cookies))
    #     f1 = open('cookieadmin.txt', 'w')
    #     f1.write(json.dumps(cookies))
    #     f1.close
    #     f1 = open('cookieadmin.txt')
    #     cookie = f1.read()
    #     cookie = json.loads(cookie)
    #     for c in cookie:
    #         driver.add_cookie(c)
    #     driver.refresh()
    #     driver.implicitly_wait(20)
    #     driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
    #
    #     # Create new chemistry experiment
    #     driver.find_element_by_id('createNewNotebookLeftNavButton').click()
    #     driver.find_element_by_id('notebookName').send_keys('Test_Note_book_QW')
    #     driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
    #     driver.find_element_by_name('createNotebook').click()

        # test_value = driver.find_element_by_id('NotebookTitle').text
        # print(test_value)
        # a = 'Test_Note_book_QW'
        # test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        # b = 'System Administrator'
        # test_value3 = driver.find_element_by_id('notebookDescription').text
        # print(test_value2)
        # c = 'Test Script execution-01/01/2019'
        #
        # if a in test_value and b in test_value2 and c in test_value3:
        #     valid = True
        # else:
        #     valid = False
        #     picture_name = 'testcreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
        #     driver.get_screenshot_as_file(picture_name)
        # self.assertTrue(valid)
        # driver.close()

    def testsharenotebookjoe(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieadmin.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.implicitly_wait(20)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_id('navMyNotebooksLink').click()
        driver.find_element_by_css_selector('#navMyNotebooks > ul > li:nth-child(1) > a').click()
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('listGroupCheckUser-1786').click()
        driver.find_element_by_xpath('//*[@id="groupsDiv"]/div[3]/input').click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath('//*[@id="shareForm"]/input[8]').click()
        time.sleep(1)
        assert driver.find_element_by_class_name('userName').is_displayed()
        assert driver.find_element_by_class_name('userTitle').is_displayed()
        assert driver.find_elements_by_id('newPermissions')[0].is_displayed()
        driver.close()

    def testsharenotebookjane(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieadmin.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.implicitly_wait(20)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # driver.find_element_by_id('navMyNotebooksLink').click()
        driver.find_element_by_css_selector('#navMyNotebooks > ul > li:nth-child(1) > a').click()

        # Share test_admin with Jane Biologist
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('listGroupCheckUser-1787').click()
        driver.find_element_by_xpath('//*[@id="groupsDiv"]/div[3]/input').click()

        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath('//*[@id="shareForm"]/input[8]').click()
        time.sleep(1)
        assert driver.find_elements_by_class_name('userName')[1].is_displayed()
        assert driver.find_element_by_class_name('userTitle').is_displayed()
        assert driver.find_elements_by_id('newPermissions')[0].is_displayed()

        # Logout
        driver.find_element_by_link_text('Logout').click()
        driver.close()


