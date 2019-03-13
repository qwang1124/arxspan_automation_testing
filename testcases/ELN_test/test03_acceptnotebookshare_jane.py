# Test ID: testELN-03
# Test name: Jane has accept the note book share by Admin Test
# Expect output:
#      1. Check received invitation from Admin ;
#      2. Successful accept the note book share request send by Admin;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Click on the invitation;
#      5. Select the note book name which shared by Admin;
#      6. Accept the share notification.
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import platform
import json


class TestNotebookJane(unittest.TestCase):
    # def setUp(self):
    #     chrome_options = Options()
    #     chrome_options.add_argument('--no-sandbox')
    #     chrome_options.add_argument("--headless")
    #     chrome_options.add_argument('--disable-gpu')
    #     if platform.system() == 'Windows':
    #         self.driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    #     elif platform.system() == "Darwin":
    #         self.driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
    #     else:
    #         self.driver = webdriver.Chrome('/usr/bin/chromedriver', chrome_options=chrome_options)
    #
    #     self.driver.implicitly_wait(3)
    #     self.base_url = "https://model.arxspan.com/login.asp"
    #     self.verificationErrors = []
    #     self.accept_next_alert = True

    def test1(self):
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get('https://model.arxspan.com/login.asp')

        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)

        cookies = driver.get_cookies()
        print(type(cookies))
        # print ("".join(cookies))
        f1 = open('cookiejane.txt', 'w')
        f1.write(json.dumps(cookies))
        f1.close

        f1 = open('cookiejane.txt')
        cookie = f1.read()
        cookie = json.loads(cookie)
        for c in cookie:
            driver.add_cookie(c)
        driver.refresh()
        driver.implicitly_wait(10)
        driver.find_element_by_link_text('Invitations').click()
        WebDriverWait(driver, 6).until(lambda driver: driver.find_element_by_xpath('//*[@id="SummaryTable"]/tbody/tr'
                                                                                   '/td[1]/a')).click()
        # accept the note book share
        driver.switch_to.window(driver.window_handles[1])
        driver.find_element_by_css_selector('#acceptForm > input:nth-child(3)').click()
        driver.close()





