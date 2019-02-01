import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestCreateexperimentJoe(unittest.TestCase):
    @allure.testcase('createexperiment')
    def test1(self):
        driver = testjoelogin()
        driver.find_element_by_id('createNewExperimentLeftNavButton').click()
        select = Select(driver.find_element_by_id('newExperimentNotebookId'))
        select.select_by_visible_text('notebook_Qing0124')
        select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
        select1.select_by_visible_text('Chemistry')
        create = driver.find_element_by_css_selector('#newExperimentDiv > form > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        create.send_keys(Keys.ENTER)
        # self.assertIn('Test_Notebook_QingWang - 004', driver.find_element_by_id('e_name').text)
        driver.close()

    # add note
    @allure.testcase('addnote')
    def test2(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        driver.find_element_by_id('addNoteButton').click()
        time.sleep(1)
        text = driver.find_element_by_id('cke_250_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#note_p_1693 > div.attachmentTableButtons > a:nth-child(1)')
        button.submit()
        time.sleep(2)
        # assert driver.find_element_by_class_name('yui3-skin-sam').is_displayed()
        driver.close()

    # upload
    @allure.testcase('uploadreaction')
    def test3(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        driver.find_element_by_id('e_details').send_keys('test')
        driver.find_element_by_id('uploadReaction').click()
        path = Path('resources//06 epoxide opening.cdx').absolute()
        driver.find_element_by_id('rxnFile').send_keys(str(path))
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        time.sleep(2)
        self.assertIn('test', driver.find_element_by_id('e_details').text)
        driver.close()

    @allure.testcase('addfile')
    def test4(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        driver.find_element_by_id('addFile_tab').click()
        text = driver.find_element_by_id('cke_2_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\nmrketalreduction21H.txt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        driver.find_element_by_class_name('resumableUploadButton').click()
        time.sleep(2)
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        time.sleep(1)
        driver.close()

    @allure.testcase('signandwitness')
    def test5(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        save = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        save.send_keys(Keys.ENTER)
        time.sleep(2)
        # assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        time.sleep(4)
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(2)
        # assert driver.find_element_by_id('historyNavLink').is_displayed()

        # logout
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235364')
        driver.find_element_by_link_text('Logout').click()
        time.sleep(1)
        driver.close()


def testjoelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

