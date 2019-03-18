# Test ID: testELN-09
# Test name: Create analytical biology_concept_experiments by Joe and upload files and send witness request to Jane Test
# Expect output:
#      1. Create a new analytical biology_concept_experiments;
#      2. Add a new note to the biology_concept_experiments;
#      3. Successful uploading, removing, downloading, replacing several kinds of files to the biology_concept_experiments;
#      4. Sign and send the witness request to Jane;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebooks;
#      5. Create a new analytical biology_concept_experiments;
#      6. Add a new note to the biology_concept_experiments;
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
from pathlib import Path


class TestanalyticalexpernimentJoe(unittest.TestCase):
    @allure.testcase('createanalyticalexperniment')
    def test1(self):
        driver = joelogin()
        driver.implicitly_wait(20)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # Select the recently note book
        driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()

        # Select to create a new analytical biology_concept_experiments
        button = driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(5)')
        button.click()

        # Add a new note
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[6]
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        save = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        save.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()

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
        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('attachmentTable_tab'))
        driver.execute_script("arguments[0].click();", button)
        # remove the file
        remove = WebDriverWait(driver, 20).until(ec.visibility_of_element_located((By.CLASS_NAME, "littleButton")))
        remove.click()
        driver.find_element_by_class_name('confirm').click()
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
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.get('https://model.arxspan.com/login.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()

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
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.get('https://model.arxspan.com/login.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()

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
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.get('https://model.arxspan.com/login.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()
        # download the file
        driver.find_element_by_id('attachmentTable_tab').click()
        driver.find_elements_by_link_text('Download')[0].click()
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

        # Sign & Close, selecting Jane Biologist as the Witness
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(3)

        # Log out
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def joelogin():
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



