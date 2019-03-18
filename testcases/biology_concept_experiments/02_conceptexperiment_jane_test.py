# Test ID: test-01
# Test name: Create Concept biology_concept_experiments by Joe and upload files and send witness request to Joe Test
# Expect output:
#      1. Create a new Concept biology_concept_experiments;
#      2. Successful uploading, removing, downloading, replacing several kinds of files to the biology_concept_experiments;
#      3. Add a new note to the upload file;
#      4. Add a new note to the biology_concept_experiments;
#      4. Sign and send the witness request to Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebooks;
#      5. Create a new concept biology_concept_experiments;
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
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import platform
from pathlib import Path
import json


class TestcoceptexpernimentJane(unittest.TestCase):
    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument("--headless")
        chrome_options.add_argument('--disable-gpu')
        if platform.system() == 'Windows':
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
        elif platform.system() == "Darwin":
            self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
        else:
            self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)

        self.driver.implicitly_wait(20)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_create_conceptexperiment_jane(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # Create a new concept experiment
        driver.find_element_by_xpath('//*[@id="navSharedNotebooks"]/ul/li[1]/a').click()
        driver.find_element_by_css_selector('#pageContentTD > div > div.createExperimentDiv > a:nth-child(4)').click()
        # Add the description to the experiment
        driver.find_element_by_id('e_details').send_keys('TESTING')
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def test_addtxtfile(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()

        # Upload the "nmrketalreduction21H.txt" file
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('addFile_tab')).click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources//nmrketalreduction21H.txt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        time.sleep(3)
        element = WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('attachmentTable_tab'))
        driver.execute_script("arguments[0].click();", element)

        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def test_adddocfile(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()
        # Upload the "GeneralFACSprotocol.doc" file
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_id('addFile_tab')).click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources//GeneralFACSprotocol.doc').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        time.sleep(2)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        time.sleep(3)
        # add a new note to the file
        text = driver.find_element_by_id('cke_2_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        time.sleep(3)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def test_addnewnote(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()
        # Add a new note to the biology_concept_experiments
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[4]

        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def test_signwitness(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        WebDriverWait(driver, 10).until(lambda driver: driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul'
                                                                                    '/li[1]/a')).click()
        # Sign & Close, selecting Joe Chemistry as the Witness
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
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
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        time.sleep(1)
        # log out
        driver.find_element_by_link_text('Logout').click()
        driver.close()



