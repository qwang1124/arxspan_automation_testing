# Test ID: testELN-04
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
import allure
from pathlib import Path


class TestCreateexperimentJoe(unittest.TestCase):
    @allure.testcase('createexperiment')
    def test1(self):
        driver = joelogin()
        driver.implicitly_wait(30)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')

        # Create new chemistry experiment
        driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()
        driver.find_element_by_css_selector(
            '#pageContentTD > div > div.createExperimentDiv > a:nth-child(2)').click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))

        # add a new note to the experiment
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[5]
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()

        # upload the reaction
        driver.find_element_by_id('uploadReaction').click()
        path = Path('resources//06 epoxide opening.cdx').absolute()
        driver.find_element_by_id('rxnFile').send_keys(str(path))
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()

        # Upload the "nmrketalreduction21H.txt" file
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources\\nmrketalreduction21H.txt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(4)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))

        # add a new note to the experiment
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[5]
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        time.sleep(1)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)

        # Sign & Close, selecting Jane Biologist as the Witness
        sign = WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        time.sleep(2)
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        checkbox = driver.find_element_by_css_selector(
            '#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        time.sleep(3)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # time.sleep(2)
        # logout
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
