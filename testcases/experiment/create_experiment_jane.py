import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


class TestCreateexperimentJane(unittest.TestCase):

    # def test_createexperiment_jane(self):
    #     driver = testjanelogin()
    #     driver.get('https://model.arxspan.com/arxlab/show-notebook.asp?id=10799')
    #     driver.find_element_by_link_text('Biology Experiment').click()
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
    #     driver.find_element_by_id('e_details').send_keys('TESTING')

    def test_addprotocolfile_jane(self):
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

    def test_addhistologyfile_jane(self):
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

    def test_addhistologyanalysis_jane(self):
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

    def test_addXenograft_jane(self):
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

    def test_createexperiment_Jane(self):
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
