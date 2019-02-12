import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestCreateexperimentJane(unittest.TestCase):

    # @allure.testcase('createexperiment')
    # def test1(self):
    #     driver = testjanelogin()
    #     time.sleep(1)
    #     driver.find_element_by_id('createNewExperimentLeftNavButton').click()
    #     select = Select(driver.find_element_by_id('newExperimentNotebookId'))
    #     select.select_by_visible_text('test_note_book_Q')
    #     type1 = Select(driver.find_element_by_id('newExperimentTypeList'))
    #     time.sleep(1)
    #     type1.select_by_visible_text('Biology')
    #     driver.find_element_by_css_selector('#newExperimentDiv > form > section.bottomButtons.buttonAlignedRight > '
    #                                         'button').click()
    #     driver.find_element_by_id('e_details').send_keys('TESTING')
    #     driver.find_element_by_css_selector('#submitRow > a:nth-child(1)').send_keys(Keys.ENTER)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.close()

    # @allure.testcase('addprotocolnote')
    # def test2(self):
    #     driver = testjanelogin()
    #     driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
    #                                  '1]/td[2]/a').click()
    #     time.sleep(2)
    #
    #     elm = driver.find_element_by_id('cke_17_contents')
    #     time.sleep(6)
    #     elm.click()
    #     time.sleep(2)
    #     driver.execute_script("arguments[0].innerText = 'TESTING TESTING'", elm)
    #     time.sleep(1)
    #     button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
    #     button.send_keys(Keys.ENTER)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.close()

    # @allure.testcase('addprotocolfile')
    # def test3(self):
    #     driver = testjanelogin()
    #     driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
    #                                  '1]/td[2]/a').click()
    #     driver.find_element_by_id('addFile_tab').click()
    #     fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
    #     driver.execute_script(
    #         'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
    #         fileinput)
    #     path = Path('resources\\GeneralFACSprotocol.doc').absolute()
    #     driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')\
    #         .send_keys(str(path))
    #     time.sleep(2)
    #     button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
    #                                                  'section.bottomButtons.buttonAlignedRight > button')
    #     button.click()
    #     # check attachment is successful and displayed
    #     driver.find_element_by_id('attachmentTable_tab').click()
    #     assert driver.find_element_by_id('attachmentTable').is_displayed
    #     # remove the file
    #     driver.find_element_by_class_name('littleButton').click()
    #     driver.find_element_by_class_name('confirm').click()
    #     driver.close()

    # @allure.testcase('addhistologyfile')
    # def test4(self):
    #     driver = testjanelogin()
    #     driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
    #                                  '1]/td[2]/a').click()
    #     driver.find_element_by_id('addFile_tab').click()
    #     fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
    #     driver.execute_script(
    #         'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
    #         fileinput)
    #     path = Path('resources\\Alports_Histology.ppt').absolute()
    #     driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
    #         .send_keys(str(path))
    #     time.sleep(2)
    #     button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
    #                                                  'section.bottomButtons.buttonAlignedRight > button')
    #     button.click()
    #     time.sleep(6)
    #     driver.find_element_by_id('attachmentTable_tab').click()
    #     link = driver.find_elements_by_xpath('//a[contains(@id, "name_quick_link")]')[0]
    #     link.click()
    #     time.sleep(2)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.close()

    # @allure.testcase('addhistologyanalysis')
    # def test5(self):
    #     driver = testjanelogin()
    #     driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
    #                                  '1]/td[2]/a').click()
    #     driver.find_element_by_id('addFile_tab').click()
    #     fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
    #     driver.execute_script(
    #         'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
    #         fileinput)
    #     path = Path('resources\\AlportsHistologyAnalysis.pdf').absolute()
    #     driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
    #         .send_keys(str(path))
    #     time.sleep(2)
    #     button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
    #                                                  'section.bottomButtons.buttonAlignedRight > button')
    #     button.click()
    #     # check attachment is successful and displayed
    #     time.sleep(6)
    #     driver.find_element_by_id('attachmentTable_tab').click()
    #     assert driver.find_element_by_id('attachmentTable').is_displayed
    #     time.sleep(2)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.close()

    @allure.testcase('addXenograft')
    def test6(self):
        driver = testjanelogin()
        driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
                                     '1]/td[2]/a').click()
        # driver.find_element_by_id('addFile_tab').click()
        # fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
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
        # check attachment is successful and displayed
        # driver.find_element_by_id('attachmentTable_tab').click()
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        # button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        # button.send_keys(Keys.ENTER)
        # time.sleep(6)
        # download the file
        driver.find_element_by_id('attachmentTable_tab').click()
        # driver.find_elements_by_xpath('//*[contains(@id, "file_9")]/td[4]/a[3]')[0].click()
        # time.sleep(4)
        # Make an edit to the file and save it locally and upload again
        driver.find_elements_by_xpath('//*[contains(@id, "file_9")]/td[4]/a[2]')[0].click()
        field = driver.find_elements_by_xpath('//input[contains(@id, "file1_9")]')[0]
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_elements_by_xpath('//input[contains(@id, "file1_9")]')[0].send_keys(str(path))
        time.sleep(4)
        button = driver.find_element_by_xpath('//*[[contains(@id, "addFileDiv_9")]/form/section[2]/button')
        button.submit()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        driver.close()
    #
    # @allure.testcase('signandwitness')
    # def test7(self):
    #     driver = testjanelogin()
    #     driver.find_element_by_xpath('//*[@id="pageContentTD"]/div/table/tbody/tr[1]/td/div/div[2]/table/tbody/tr['
    #                                      '1]/td[2]/a').click()
    #     driver.find_element_by_xpath("//a[contains(@onclick = 'clickSave();')]").click()
    #     driver.find_element_by_id('signExperimentButton').click()
    #     select = Select(driver.find_element_by_id('signStatusBox'))
    #     select.select_by_visible_text('Sign and Close')
    #     select = Select(driver.find_element_by_id('requesteeIdBox'))
    #     select.select_by_visible_text('Jane Biologist')
    #     driver.find_element_by_xpath("//button[contains(@onclick = \'clickSign();\')]").click()
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.find_element_by_id('makePDFLink').click()
    #
    #     # logout
    #     driver.find_element_by_link_text('Logout').click()
    #     driver.close()


def testjanelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/test_login.asp')
    # driver.maximize_window()
    driver.find_element_by_id('test_login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
    return driver
