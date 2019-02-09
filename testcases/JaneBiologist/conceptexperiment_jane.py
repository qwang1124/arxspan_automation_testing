import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestcoceptexpernimentJane(unittest.TestCase):
    @allure.testcase('createconceptexperiment')
    def test1(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/show-Admin.asp?id=10800')
        driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(4)').click()
        driver.find_element_by_id('e_details').send_keys('TESTING')
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        self.assertIn('TESTING', driver.find_element_by_id('e_details').text)

    @allure.testcase('conceptexperimentaddfile')
    def test2(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/free-JaneBiologist.asp?id=2375')
        time.sleep(1)
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\nmrketalreduction21H.txt').absolute()
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

    @allure.testcase('conceptexperimentaddfile2')
    def test3(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/free-JaneBiologist.asp?id=2375')
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\GeneralFACSprotocol.doc').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        text = driver.find_element_by_id('cke_2_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.close()

    @allure.testcase('conceptexperimentaddnote')
    def test4(self):
        driver = testjanelogin()
        driver.get('https://model.arxspan.com/arxlab/free-JaneBiologist.asp?id=2375')
        text = driver.find_element_by_id('cke_17_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('jane@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Joe Chemist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(1)
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver

