# Test ID: test-01
# Test name: Create analytical experiment by Joe and upload files and send witness request to Jane Test
# Expect output:
#      1. Create a new analytical experiment;
#      2. Add a new note to the experiment;
#      3. Successful uploading, removing, downloading, replacing several kinds of files to the experiment;
#      4. Sign and send the witness request to Jane;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebook;
#      5. Create a new analytical experiment;
#      6. Add a new note to the experiment;
#      7. Upload the "PushTestingProtocolforELN.docx";
#      8. Remove the "PushTestingProtocolforELN.docx";
#      9. Upload the "AlportsHistologyAnalysis.pdf";
#     10. Upload the "~$Xenograft.xls";
#     11. Download the "~$Xenograft.xls";
#     12. Replace the "~$Xenograft.xls" to "InventoryBulkUpdate.xlsx";
#     13. Sign & Close, selecting Jane Biologist as the Witness;
#     14. Log out.
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure
from pathlib import Path


class TestanalyticalexpernimentJoe(unittest.TestCase):
    @allure.testcase('createanalyticalexperniment')
    def test1(self):
        driver = testjoelogin()
        time.sleep(2)
        # Select the recently note book
        driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()
        time.sleep(1)
        # Select to create a new analytical experiment
        button = driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(5)')
        button.click()
        time.sleep(2)
        # Add a new note
        text = driver.find_element_by_id('cke_17_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        save = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        save.send_keys(Keys.ENTER)
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()

        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Add "PushTestingProtocolforELN.docx" file
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
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        # remove the file
        driver.find_element_by_class_name('littleButton').click()
        time.sleep(2)
        driver.find_element_by_class_name('confirm').click()
        time.sleep(2)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Upload the "Alports_Histology.ppt" file
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
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # driver.find_element_by_id('attachmentTable_tab').click()
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Upload the "AlportsHistologyAnalysis.pdf" file
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
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # driver.find_element_by_id('attachmentTable_tab').click()
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Upload the "~$Xenograft.xls" file
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
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # driver.find_element_by_id('attachmentTable_tab').click()
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(4)
        # download the file
        driver.find_element_by_id('attachmentTable_tab').click()
        driver.find_element_by_xpath('//*[contains(@id, "file_2")]/td[4]/a[3]').click()
        time.sleep(4)
        # Replace the file
        driver.find_elements_by_link_text('Replace')[0].click()
        field = driver.find_elements_by_xpath('//*[contains(@id, "file1_2")]')[0]
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_elements_by_xpath('//*[contains(@id, "file1_2")]')[0].send_keys(str(path))
        time.sleep(4)
        button = driver.find_element_by_xpath('//*[contains(@id, "addFileDiv_2")]/form/section[2]/button')
        button.submit()
        time.sleep(2)
        assert driver.find_element_by_id('attachmentTable').is_displayed
        time.sleep(2)
        # Sign & Close, selecting Jane Biologist as the Witness
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(4)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        time.sleep(2)
        select.select_by_visible_text('Jane Biologist')
        time.sleep(1)
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # Log out
        driver.find_element_by_link_text('Logout').click()
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



