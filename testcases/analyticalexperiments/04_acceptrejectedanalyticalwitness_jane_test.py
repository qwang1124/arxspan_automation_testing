# Test ID: test-01
# Test name: Jane has accept the analytical biology_concept_experiments witness request by Joe Test
# Expect output:
#      1. Check received witness request from Joe is showing ;
#      2. Successful accept witness request send by Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Check the witness request is showing the notification;
#      5. Select the analytical biology_concept_experiments name which shared by Joe;
#      6. Accept the witness request
#      7. Log out.
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


class TestWitnessJane(unittest.TestCase):
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

        self.driver.implicitly_wait(10)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_accept_rejected_analyticalwitness_jane(self):
        driver = self.driver
        driver.get(self.base_url)
        f1 = open('cookieajane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        # check the witness requests is showing the notification
        assert driver.find_element_by_id('witnessRequestsHolder').is_displayed()
        time.sleep(2)
        # select the analytical experiment name
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        sign = WebDriverWait(driver, 6).until(ec.visibility_of_element_located((By.CSS_SELECTOR, "#witnessButtons > "
                                                                                                 "a:nth-child(1)")))
        driver.execute_script("arguments[0].click();", sign)

        # sign and witness
        email = driver.find_elements_by_id('signEmail')[1]
        email.send_keys('jane@demo.com')
        password = driver.find_elements_by_id('password')[1]
        password.send_keys('carbonCopee')
        form = driver.find_element_by_id('witnessForm')
        form.click()
        driver.find_element_by_id('witnessSubmitButton').click()
        driver.get('https://model.arxspan.com/login.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        # Log out
        driver.find_element_by_link_text('Logout').click()
        driver.close()

