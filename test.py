import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
from pathlib import Path


class TestCreateexperimentJane(unittest.TestCase):

    def test1(self):
        driver = janelogin()
        driver.implicitly_wait(30)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "addFile_tab"))).click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\~$Xenograft.xls').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(3)
        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('attachmentTable_tab'))
        driver.execute_script("arguments[0].click();", button)
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "Download"))).click()
        time.sleep(2)
        # Replace the file
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.LINK_TEXT, "Replace"))).click()
        field = driver.find_elements_by_xpath('//input[contains(@id, "file1_10")]')[0]
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_elements_by_xpath('//input[contains(@id, "file1_10")]')[0].send_keys(str(path))
        button = driver.find_element_by_xpath('//*[contains(@id, "addFileDiv_10")]/form/section[2]/button')
        button.submit()
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)


def janelogin():
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
