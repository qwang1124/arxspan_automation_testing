# Test ID: test-01
# Test name: Create chemistry experiment by Joe and upload files and send witness request to Joe Test
# Expect output:
#      1. Create a new Biologist experiment;
#      2. Add a new note to the experiment;
#      3. Upload a new reaction to the experiment;
#      4. Successful uploading, removing, downloading, replacing several kinds of files to the experiment;
#      5. Sign and send the witness request to Jane;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebook;
#      5. Create a new chemistry experiment;
#      6. Add a new note to the experiment;
#      7. Upload the reaction;
#      8. Upload the "nmrketalreduction21H.txt";
#      9. Add a new note toe the experiment;
#     10. Sign & Close, selecting Jane Biologist as the Witness;
#     11. Log out.
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
        time.sleep(1)
        # Create new chemistry experiment
        driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()
        driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(2)').click()
        time.sleep(2)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        time.sleep(2)
        # add a new note to the experiment
        driver.find_element_by_id('addNoteButton').click()
        time.sleep(1)
        text = driver.find_element_by_id('cke_250_contents')
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        time.sleep(1)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)
        time.sleep(4)
        assert driver.find_element_by_id('historyNavLink').is_displayed()

        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # upload the reaction
        driver.find_element_by_id('uploadReaction').click()
        path = Path('resources//06 epoxide opening.cdx').absolute()
        driver.find_element_by_id('rxnFile').send_keys(str(path))
        time.sleep(2)
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        time.sleep(2)
        assert driver.find_element_by_id('historyNavLink').is_displayed()

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
        # assert driver.find_element_by_id('historyNavLink').is_displayed()
        # driver.find_element_by_id('attachmentTable_tab').click()
        # assert driver.find_element_by_id('attachmentTable').is_displayed
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        time.sleep(6)

    # @allure.testcase('signandkeepopen')
    # def test5(self):
    #     driver = testjoelogin()
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
    #     time.sleep(2)
    #     save = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
    #     save.send_keys(Keys.ENTER)
    #     time.sleep(2)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
    #     time.sleep(2)
    #     driver.find_element_by_id('signExperimentButton').click()
    #     email = driver.find_elements_by_id('signEmail')[0]
    #     email.send_keys('joe@demo.com')
    #     password = driver.find_elements_by_id('password')[0]
    #     password.send_keys('carbonCopee')
    #     select = Select(driver.find_element_by_id('signStatusBox'))
    #     select.select_by_visible_text('Sign and Keep Open')
    #     checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
    #     checkbox.click()
    #     time.sleep(4)
    #     driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
    #     time.sleep(4)
    #     driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
    #     time.sleep(2)
    #     driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
    #     time.sleep(4)
    #     assert driver.find_element_by_id('historyNavLink').is_displayed()
    #     driver.close()

        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        # add a new note to the experiment
        driver.find_element_by_id('addNoteButton').click()
        time.sleep(1)
        text = driver.find_element_by_id('cke_250_contents')
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        time.sleep(1)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)
        time.sleep(6)
        # Sign & Close, selecting Jane Biologist as the Witness
        driver.find_element_by_id('signExperimentButton').click()
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        time.sleep(4)
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(4)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(4)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        # logout
        driver.find_element_by_link_text('Logout').click()
        time.sleep(1)
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

