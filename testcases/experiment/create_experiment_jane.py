import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestCreateexperimentJane(unittest.TestCase):

    @allure.testcase('createexperiment')
    def test1(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/show-notebook.asp?id=10799')
        driver.find_element_by_link_text('Biology Experiment').click()
        driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
        driver.find_element_by_id('e_details').send_keys('TESTING')
        self.assertIn('TESTING', driver.find_element_by_id('e_details').text)

    @allure.testcase('addprotocolfile')
    def test2(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        elm = driver.find_element_by_id('file1')
        elm.send_keys('C:\\Users\\QingW\\Downloads\\PushTestingProtocolforELN.docx')
        time.sleep(2)
        button = driver.find_element_by_css_selector('#addFileDiv > form > section.bottomButtons.buttonAlignedRight > '
                                                     'button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_p_15661_name_quick_link').click().is_displayed()
        # remove the file
        driver.find_element_by_class_name('littleButton').click()

    @allure.testcase('addhistologyfile')
    def test3(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        elm = driver.find_element_by_id('file1')
        elm.send_keys('C:\\Users\\QingW\\Downloads\\fwdtestscriptsandtestingfiles\\Alports_Histology.ppt')
        time.sleep(2)
        button = driver.find_element_by_css_selector('#addFileDiv > form > section.bottomButtons.buttonAlignedRight > '
                                                     'button')
        button.click()
        driver.find_element_by_id('attachmentTable_tab').click()

    @allure.testcase('addhistologyanalysis')
    def test4(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        elm = driver.find_element_by_id('file1')
        elm.send_keys('C:\\Users\\QingW\\Downloads\\fwdtestscriptsandtestingfiles\\Alports Histology Analysis.pdf')
        time.sleep(2)
        button = driver.find_element_by_css_selector('#addFileDiv > form > section.bottomButtons.buttonAlignedRight > '
                                                      'button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()

    @allure.testcase('addXenograft')
    def test5(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        elm = driver.find_element_by_id('file1')
        elm.send_keys('C:\\Users\\QingW\\Downloads\\fwdtestscriptsandtestingfiles\\~$Xenograft.xls')
        time.sleep(2)
        button = driver.find_element_by_css_selector('#addFileDiv > form > section.bottomButtons.buttonAlignedRight > '
                                                     'button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        # download the file
        driver.find_element_by_class_name('littleButton').click()

    @allure.testcase('signandwitness')
    def test6(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com//arxlab//show-notebook.asp?id=10753')
        driver.find_element_by_link_text('Biology Experiment').click()

        driver.find_element_by_id('createNewExperimentLeftNavButton').click()
        select = Select(driver.find_element_by_id('newExperimentNotebookId'))
        select.select_by_visible_text('Test_Notebook_QingWang')
        select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
        select1.select_by_visible_text('Chemistry')
        driver.find_element_by_tag_name('button').click()

        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('signStatusBox'))
        select.select_by_visible_text('Sign and Close')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()
        # self.assertIn('1/14/2019 09:36:41 PM', driver.find_element_by_id('hd_9_235143').text)

        # logout
        driver.find_element_by_link_text('Logout').click()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
