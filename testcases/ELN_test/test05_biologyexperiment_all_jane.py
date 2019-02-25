# Test ID: testELN-05
# Test name: Create Biologist experiment by Jane and upload files and send witness request to Joe Test
# Expect output:
#      1. Create a new Biologist experiment;
#      2. Add a new protocol note to the experiment;
#      3. Successful uploading, removing, downloading, replacing several kinds of files to the experiment;
#      4. Sign and send the witness request to Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebook;
#      5. Create a new Biologist experiment;
#      6. Add a new protocol note to the experiment;
#      7. Upload the "GeneralFACSprotocol.doc";
#      8. Remove the "GeneralFACSprotocol.doc";
#      9. Upload the "Alports_Histology.ppt";
#     10. Upload the "AlportsHistologyAnalysis.pdf";
#     11. Upload the "~$Xenograft.xls";
#     12. Download the "~$Xenograft.xls";
#     13. Replace the "~$Xenograft.xls" to "InventoryBulkUpdate.xlsx";
#     14. Sign & Close, selecting Jane Biologist as the Witness;
#     15. Log out.
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

    @allure.testcase('createexperiment')
    def test1(self):
        driver = janelogin()
        driver.implicitly_wait(20)

        # Create new Biologist experiment
        driver.find_element_by_xpath('//*[@id="navSharedNotebooks"]/ul/li[1]/a').click()
        driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(3)').click()
        driver.find_element_by_id('e_details').send_keys('TESTING')
        driver.find_element_by_css_selector('#submitRow > a:nth-child(1)').send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()

        # Add a new protocol note
        elm = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[4]
        elm.click()
        driver.execute_script("arguments[0].innerText = 'TESTING TESTING'", elm)

        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()

        # Upload the "GeneralFACSprotocol.doc" file
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\GeneralFACSprotocol.doc').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        button = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('attachmentTable_tab'))
        driver.execute_script("arguments[0].click();", button)

        # remove the file
        WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.CLASS_NAME, "littleButton"))).click()
        driver.find_element_by_class_name('confirm').click()
        time.sleep(2)

        # Upload the "Alports_Histology.ppt" file
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\Alports_Histology.ppt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.get('https://model.arxspan.com/login.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()

        # Upload the "AlportsHistologyAnalysis.pdf" file
        driver.find_element_by_id('addFile_tab').click()
        fileinput = driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\AlportsHistologyAnalysis.pdf').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        # Upload the "~$Xenograft.xls" file
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
        driver.find_element_by_link_text('Download').click()
        time.sleep(2)
        # Replace the file
        driver.find_element_by_link_text('Replace').click()
        field = driver.find_elements_by_xpath('//input[contains(@id, "file1_10")]')[0]
        driver.execute_script("arguments[0].style.display = 'block';", field)
        path = Path('resources\\InventoryBulkUpdate.xlsx').absolute()
        driver.find_elements_by_xpath('//input[contains(@id, "file1_10")]')[0].send_keys(str(path))
        button = driver.find_element_by_xpath('//*[contains(@id, "addFileDiv_10")]/form/section[2]/button')
        button.submit()
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)

        # Sign & Close, selecting Joe Chemist as the Witness
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('jane@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('signStatusBox'))
        select.select_by_visible_text('Sign and Close')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Joe Chemist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        time.sleep(1)

        # logout
        driver.find_element_by_link_text('Logout').click()
        driver.close()


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
