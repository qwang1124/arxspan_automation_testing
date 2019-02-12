import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestanalyticalexpernimentJane(unittest.TestCase):
    @allure.testcase('createanalyticalexperniment')
    def test1(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/show-test_admin.asp?id=10800')
        button = driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(5)')
        button.click()
        text = driver.find_element_by_id('cke_17_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        save = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        save.send_keys(Keys.ENTER)
        time.sleep(1)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.close()

    @allure.testcase('analyticalexpernimentaddfile')
    def test2(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\PushTestingProtocolforELN.docx').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        # remove the file
        driver.find_element_by_class_name('littleButton').click()
        driver.find_element_by_class_name('confirm').click()

        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.close()

    @allure.testcase('analyticalexpernimentaddfile2')
    def test3(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
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
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.close()

    @allure.testcase('analyticalexpernimentaddfile3')
    def test4(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
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
        time.sleep(1)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.close()

    @allure.testcase('analyticalexpernimentaddfile4')
    def test4(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
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
        time.sleep(1)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        # download the file
        driver.find_element_by_id('attachmentTable_tab').click()

        driver.find_element_by_xpath('//*[@id="file_2497_tr"]/td[4]/a[3]').click()

        # Make an edit to the file and save it locally and upload again
        driver.find_element_by_xpath('//*[@id="file_2497_tr"]/td[4]/a[2]').click()
        field = driver.find_element_by_id('file1_2497')
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_element_by_id('file1_2497').send_keys(str(path))
        button = driver.find_element_by_xpath('//*[@id="addFileDiv_2497"]/form/section[2]/button')
        button.submit()
        time.sleep(1)
        assert driver.find_element_by_id('attachmentTable').is_displayed
        driver.close()

    @allure.testcase('analyticalexpernimentwitness')
    def test5(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(1)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(1)
        driver.get('https://model.arxspan.com/arxlab/anal-test_JaneBiologist.asp?id=946')
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjoelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/test_login.asp')
    driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    return driver

