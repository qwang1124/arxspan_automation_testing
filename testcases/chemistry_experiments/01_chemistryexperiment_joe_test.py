# Test ID: test-01
# Test name: Create chemistry biology_concept_experiments by Joe and upload files and send witness request to Joe Test
# Expect output:
#      1. Create a new Biologist biology_concept_experiments;
#      2. Add a new note to the biology_concept_experiments;
#      3. Upload a new reaction to the biology_concept_experiments;
#      4. Successful uploading, removing, downloading, replacing several kinds of files to the biology_concept_experiments;
#      5. Sign and send the witness request to Jane;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Joe as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Select the most recent notebooks;
#      5. Create a new chemistry biology_concept_experiments;
#      6. Add a new note to the biology_concept_experiments;
#      7. Upload the reaction;
#      8. Upload the "nmrketalreduction21H.txt";
#      9. Add a new note toe the biology_concept_experiments;
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
from selenium.webdriver.chrome.options import Options
import platform
import json
from pathlib import Path


class TestCreateexperimentJoe(unittest.TestCase):
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

    def test_create_chemistryexperiment_joe(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.find_element_by_id('login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        cookies = driver.get_cookies()
        print(type(cookies))
        # print ("".join(cookies))
        f1 = open('cookieajoe.txt', 'w')
        f1.write(json.dumps(cookies))
        f1.close
        f1 = open('cookieajoe.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')

        # Create new chemistry biology_concept_experiments
        driver.find_element_by_xpath('//*[@id="navMyNotebooks"]/ul/li/a').click()
        driver.find_element_by_css_selector(
            '#pageContentTD > div > div.createExperimentDiv > a:nth-child(2)').click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def addnote(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajoe.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        # add a new note to the biology_concept_experiments
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[5]
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def uploadreaction(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajoe.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        driver.find_element_by_id('e_details').send_keys('test')
        # upload the reaction
        driver.find_element_by_id('uploadReaction').click()
        path = Path('resources//06 epoxide opening.cdx').absolute()
        driver.find_element_by_id('rxnFile').send_keys(str(path))
        driver.find_element_by_xpath("//button[contains(@onclick, 'rxnFile')]").click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def uploadfile(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajoe.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        # Upload the "nmrketalreduction21H.txt" file
        driver.find_element_by_id('addFileButton').click()
        fileinput = driver.find_elements_by_css_selector('#fileInputContainer > div > input[type="file"]')
        driver.execute_script(
            'arguments[0].style = ""; arguments[0].style.display = "block"; arguments[0].style.visibility = "visible";',
            fileinput)
        path = Path('resources//nmrketalreduction21H.txt').absolute()
        driver.find_element_by_css_selector('#fileInputContainer > div > input[type="file"]') \
            .send_keys(str(path))
        button = driver.find_element_by_css_selector('#resumableBrowserHolder > '
                                                     'section.bottomButtons.buttonAlignedRight > button')
        button.click()
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert WebDriverWait(driver, 10).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        driver.close()

    def signandwitness(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajoe.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        # add a new note to the biology_concept_experiments
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_elements_by_css_selector('[class="cke_contents cke_reset"]')[5]
        driver.execute_script("arguments[0].innerHTML='<p>this is test</p>'", text)
        time.sleep(1)
        save = driver.find_element_by_xpath('//*[contains(@id, "note_p")]/div[4]/a[1]')
        save.send_keys(Keys.ENTER)

        # Sign & Close, selecting Jane Biologist as the Witness
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.ID, "signExperimentButton")))
        driver.execute_script("arguments[0].click();", sign)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
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



