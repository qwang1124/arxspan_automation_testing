#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Input the URL of login page;
#      3. Input the Jane as the username;
#      4. Input the password;
#      5. Choose the different company;

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
import allure


class LoginTestJane(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    @allure.testcase('login test demo')
    def test1(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Demo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Demo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_2_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test CpdTrackingNoInv')
    def test2(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CpdTrackingNoInv')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CpdTrackingNoInv'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_3_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test CT DEMO')
    def test3(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CT DEMO')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CT DEMO'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_4_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test Daiichi Sankyo')
    def test4(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Daiichi Sankyo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Daiichi Sankyo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_5_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test Formulation Demo')
    def test5(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Formulation Demo')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Formulation Demo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_6_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test Model Test Script Company')
    def test6(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Model Test Script Company'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_7_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('login test Yumanity Model')
    def test7(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('login-email').send_keys('jane@demo.com')
        driver.find_element_by_id('login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Yumanity Model')
        driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Jane Biologist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Yumanity Model'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_8_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)



