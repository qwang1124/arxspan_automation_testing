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
        select.select_by_visible_text('Test_Notebook_QingWang')
        select1 = Select(driver.find_element_by_id('newExperimentTypeList'))
        select1.select_by_visible_text('Chemistry')
        driver.find_element_by_tag_name('button').click()
        self.assertIn('Test_Notebook_QingWang - 004', driver.find_element_by_id('e_name').text)
        driver.close()

    # addnote: no text insert

    # def test_addnote(self):
    #     driver = testjoelogin()
    #     driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')
    #     driver.find_element_by_id('addNoteButton').click()
    #     driver.find_element_by_id('note_p_1638_name').sendkeys('Testing')
    #     driver.find_element_by_id('cke_273').click()
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
    #
    #     # Switch to frame failed
    #
    #     # driver.switch_to.frame(driver.find_element_by_class_name('cke_wysiwyg_frame cke_reset'))
    #     # driver.switch_to.default_content()
    #     text = driver.find_element_by_css_selector('body > p')
    #     text.send_keys('11111111111')
    #     # driver.execute_script("arguments[0].innerHTML = 'Set text using innerHTML'", text)
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()

        # elm = driver.find_element_by_class_name('cke_editable cke_editable_themed cke_contents_ltr cke_show_borders')
        # elm.send_keys(Keys.TAB)
        # elm.click()
        # elm.send_keys(u'TestExperimentNote0109')
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()

        # frame = driver.find_element_by_tag_name("iframe")
        # driver.switch_to.frame(frame)
        # body = driver.find_element_by_tag_name("body")
        # body.send_keys("some test here")
        # button = driver.find_element_by_xpath('//a[@onclick="clickSave();"]')
        # button.click()
        # time.sleep(2)
        # driver.close()

    #     driver.find_element_by_id('signExperimentButton').click()
    #     select = Select(driver.find_element_by_id('signStatusBox'))
    #     select.select_by_visible_text('Sign and Close')
    #     select = Select(driver.find_element_by_id('requesteeIdBox'))
    #     select.select_by_visible_text('Jane Biologist')
    #     driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()

    # upload
    @allure.testcase('uploadreaction')
    def test3(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')

        driver.find_element_by_id('e_details').send_keys('test')
        driver.find_element_by_id('uploadReaction').click()
        path = Path('resources//06 epoxide opening.cdx').absolute()
        driver.find_element_by_id('rxnFile').send_keys(str(path))
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        self.assertIn('test', driver.find_element_by_id('e_details').text)
        driver.close()

    @allure.testcase('addfile')
    def test4(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235248')
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\nmrketalreduction21H.txt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        driver.find_element_by_class_name('resumableUploadButton').click()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('file_533152_tr').is_displayed
        # PDF only show up after save
        driver.find_element_by_id('showPDFLink').click()

        driver.close()

    @allure.testcase('signandwitness')
    def test5(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235143')
        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('signStatusBox'))
        select.select_by_visible_text('Sign and Close')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_xpath("//button[contains(@onclick = 'clickSign();')]").click()
        self.assertIn('1/14/2019 09:36:41 PM', driver.find_element_by_id('hd_9_235143').text)

        # logout
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjoelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.maximize_window()
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Demo')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

