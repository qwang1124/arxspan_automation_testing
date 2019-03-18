from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import platform
import unittest, time, re, os
import json


class TestNotebookJoe(unittest.TestCase):
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

        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_accept_notebookshare_joe(self):
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
        driver.implicitly_wait(20)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_link_text('Invitations').click()
        driver.find_element_by_css_selector('#SummaryTable > tbody > tr > td.sorting_1 > a').click()
        # accept the note book share
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_css_selector('#acceptForm > input:nth-child(3)').click()
        driver.close()




