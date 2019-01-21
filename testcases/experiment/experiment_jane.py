import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


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
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\GeneralFACSprotocol.doc').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')\
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed
        # remove the file
        driver.find_element_by_class_name('littleButton').click()
        driver.find_element_by_class_name('confirm').click()
        driver.close()

    @allure.testcase('addhistologyfile')
    def test3(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\Alports_Histology.ppt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed

        driver.close()

    @allure.testcase('addhistologyanalysis')
    def test4(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\AlportsHistologyAnalysis.pdf').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed
        driver.close()

    @allure.testcase('addXenograft')
    def test5(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\~$Xenograft.xls').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        # check attachment is successful and displayed
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed
        # download the file
        driver.find_element_by_class_name('littleButton').click()
        # Make an edit to the file and save it locally and upload again
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\~$Xenograft.xls').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed
        driver.close()

    @allure.testcase('signandwitness')
    def test6(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/bio-experiment.asp?id=31893')
        driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('signStatusBox'))
        select.select_by_visible_text('Sign and Close')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()
        # self.assertIn('1/14/2019 09:36:41 PM', driver.find_element_by_id('hd_9_235143').text)
        driver.find_element_by_id('makePDFLink').click()

        # logout
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    # driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
