import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestCreateexperimentJane(unittest.TestCase):

    def test6(self):
        driver = testjanelogin()
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()
        # time.sleep(1)
        # button = driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(5)')
        # button.click()
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # driver.find_element_by_id('addFileButton').click()
        # fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        # driver.execute_script(
        #     'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
        #     fileinput)
        # path = Path('resources\\~$Xenograft.xls').absolute()
        # driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
        #     .send_keys(str(path))
        # time.sleep(2)
        # button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
        #                                              'section.bottomButtons.buttonAlignedRight > button')
        # button.click()
        # time.sleep(6)
        # assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        time.sleep(2)
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        # button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        # button.send_keys(Keys.ENTER)
<<<<<<< HEAD
        driver.find_elements_by_link_text('Replace')[0].click()
        field = driver.find_element_by_xpath('//*[contains(@id, "file1_2")]')
=======
        # # download the file
        # time.sleep(2)
        driver.get('https://model.arxspan.com/arxlab/bio-test_JaneBiologist.asp?id=32659')
        # driver.find_element_by_id('attachmentTable_tab').click()
        #
        # driver.find_elements_by_xpath('//td[4]/a[3]')[0].click()

        # Make an edit to the file and save it locally and upload again
        content = u'这是一段自动输入的测试内容'
        js = "document.getElementByClassName('cke_wysiwyg_frame cke_reset').contentWindow. " \
             "document.getElementsByTagName('body')[0].innerHTML = ' % s'" % content
        driver.execute_script(js)

        driver.find_element_by_id('attachmentTable_tab').click()
        driver.find_elements_by_xpath('//*[contains(@id, "file_9")]/td[4]/a[2]')[0].click()
        field = driver.find_elements_by_xpath('//input[contains(@id, "file1_9")]')[0]
>>>>>>> c5e124cb3fe2cfceb7c3556c67722874ba0535ed
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_element_by_xpath('//*[contains(@id, "file1_2")]').send_keys(str(path))
        time.sleep(4)
        button = driver.find_element_by_xpath('//*[contains(@id, "addFileDiv_2")]/form/section[2]/button')
        button.submit()
        time.sleep(2)
        assert driver.find_element_by_id('attachmentTable').is_displayed
        driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/test_login.asp')
    # driver.maximize_window()
<<<<<<< HEAD
    driver.find_element_by_id('test_login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
=======
    driver.find_element_by_id('login-email').send_keys('joe@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
>>>>>>> 9000cab28c0939cb42b548cb5b94048f61bd6e68
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    return driver

