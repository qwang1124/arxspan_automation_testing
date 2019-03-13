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
import json
import requests
import pickle


# def save_cookie(driver, path):
#     with open(path, 'wb') as filehandler:
#         pickle.dump(driver.get_cookies(), filehandler)
#
#
# def load_cookie(driver, path):
#      with open(path, 'rb') as cookiesfile:
#          cookies = pickle.load(cookiesfile)
#          for cookie in cookies:
#              driver.add_cookie(cookie)

# cookies = pickle.load(open('cookie.txt', 'w'))
#
# s = requests.Session()
# for cookie in cookies:
#     s.cookies.set(cookie['name'], cookie['value'])
# response = s.get("https://model.arxspan.com/login.asp")
# bodyStr = response.text


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://model.arxspan.com/login.asp')
# f1 = open('cookieadmin.txt')
# cookie = f1.read()
# cookie = json.loads(cookie)
# for c in cookie:
#     driver.add_cookie(c)
# driver.refresh()
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




