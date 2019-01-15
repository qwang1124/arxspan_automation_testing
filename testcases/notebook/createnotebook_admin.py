import time
import unittest
from webdriver_manager.chrome import ChromeDriverManager
import allure
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select


class TestCreatenotebookAdmin(unittest.TestCase):

    @allure.testcase('test create notebook by Admin')
    def testcreatenotebook(self):
        driver = testadminlogin()

        # create notebook by admin
        driver.find_element_by_id('createNewNotebookLeftNavButton').click()
        driver.find_element_by_id('notebookName').send_keys('Test_Notebook_Q')
        driver.find_element_by_name('notebookDescription').send_keys('Test Script execution-01/01/2019')
        driver.find_element_by_name('createNotebook').click()

        test_value = driver.find_element_by_id('NotebookTitle').text
        print(test_value)
        a = 'Test_Notebook_Q'
        test_value2 = driver.find_element_by_id('notebookOwnerSpan').text
        b = 'System Administrator'
        test_value3 =driver.find_element_by_id('notebookDescription').text
        print(test_value2)
        c = 'Test Script execution-01/01/2019'

        if a in test_value and b in test_value2 and c in test_value3:
            valid = True
        else:
            valid = False
            picture_name = 'testcreateNotebookAdmin_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test share notebook to Joe')
    def testsharenotebookjoe(self):
        driver = testadminlogin()
        driver.get('https://model.arxspan.com//arxlab//show-notebook.asp?id=10733')

        # Share notebook with Joe Chemistry
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('expandGroupLink-105').click()
        driver.find_element_by_id('listGroupCheckUser-936').click()
        driver.find_element_by_xpath('//input[@type="button" and @value="Select"]').click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Share']").click()

        test_value = driver.find_element_by_class_name('userName').text
        print(test_value)
        a = 'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('userTitle').text
        b = 'System Administrator'
        test_value3 = driver.find_element_by_id('newPermissions').text
        print(test_value2)
        c = 'View/Write'

        if a in test_value and b in test_value2 and c in test_value3:
            valid = True
        else:
            valid = False
            picture_name = 'testsharenotebookjoe_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test share notebook to Joe Chemistry')
    def testsharenotebookjane(self):
        driver = testadminlogin()
        driver.get('https://model.arxspan.com//arxlab//show-notebook.asp?id=10733')

        # Share notebook with Jane Biologist
        driver.find_element_by_id('shareNotebookLink').click()
        driver.find_element_by_class_name('groupSelectLink').click()
        driver.find_element_by_id('expandGroupLink-105').click()
        driver.find_element_by_id('listGroupCheckUser-937').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Select']").click()
        driver.find_element_by_id('canRead').click()
        driver.find_element_by_id('canWrite').click()
        driver.find_element_by_xpath("//input[@type='button' and @value='Share']").click()

        test_value = driver.find_element_by_class_name('userName').text
        print(test_value)
        a = 'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('userTitle').text
        b = 'System Administrator'
        test_value3 = driver.find_element_by_id('newPermissions').text
        print(test_value2)
        c = 'View/Write'

        if a in test_value and b in test_value2 and c in test_value3:
            valid = True
        else:
            valid = False
            picture_name = 'testsharenotebookjane_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

        # Logout
        driver.find_element_by_link_text('Logout').click()


def testadminlogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('admin@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver


