import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestCreatenotebookAdmin(unittest.TestCase):

    @allure.testcase('test create test_admin by test_admin')
    def testcreatenotebook(self):
        driver = testadminlogin()

        # create test_admin by admin
        driver.find_element_by_id('createNewNotebookLeftNavButton').click()
        driver.find_element_by_id('notebookName').send_keys('Test_Notebook_Q')
        driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
        driver.find_element_by_name('createNotebook').click()

    @allure.testcase('test share test_admin to Joe')
    def testsharenotebookjoe(self):
        driver = testadminlogin()
        driver.find_element_by_id('navMyNotebooksLink').click()
        driver.find_element_by_css_selector('#navMyNotebooks > ul > li:nth-child(1) > a').click()
        # Share test_admin with Joe
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

    @allure.testcase('test share test_admin to Jane Biologist')
    def testsharenotebookjane(self):
        driver = testadminlogin()
        driver.find_element_by_id('navMyNotebooksLink').click()
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


def testadminlogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/test_login.asp')
    driver.maximize_window()
    driver.find_element_by_id('test_login-email').send_keys('admin@demo.com')
    driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    return driver
