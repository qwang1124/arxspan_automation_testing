# Test ID: test-01
# Test name: Create Concept experiment by Joe and upload files and send witness request to Joe Test
# Expect output:
#      1. Create a new Concept experiment;
#      2. Successful uploading, removing, downloading, replacing several kinds of files to the experiment;
#      3. Add a new note to the upload file;
#      4. Add a new note to the experiment;
#      4. Sign and send the witness request to Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebook;
#      5. Create a new concept experiment;
#      7. Upload the "nmrketalreduction21H.txt";
#      8. Upload the "GeneralFACSprotocol.doc";
#      9. Add a new note to the file;
#     10. Sign & Close, selecting Joe Chemistry as the Witness;
#     11. Log out.
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
        time.sleep(2)
        # Create a new concept experiment
        driver.find_element_by_xpath('//*[@id="navSharedNotebooks"]/ul/li[1]/a').click()
        driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(4)').click()
        driver.find_element_by_id('e_details').send_keys('TESTING')
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(4)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Upload the "nmrketalreduction21H.txt" file
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
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)

        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Upload the "GeneralFACSprotocol.doc" file
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\GeneralFACSprotocol.doc').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        # add a new note to the file
        text = driver.find_element_by_id('cke_2_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        time.sleep(6)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_id('attachmentTable_tab').click()
        assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)

        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # Add a new note to the experiment
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_element_by_id('cke_17_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert driver.find_element_by_id('historyNavLink').is_displayed()

        # Sign & Close, selecting Joe Chemistry as the Witness
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('jane@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        time.sleep(2)
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        time.sleep(2)
        select.select_by_visible_text('Joe Chemist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(6)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(4)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # log out
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



