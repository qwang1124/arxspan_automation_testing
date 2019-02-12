#!/usr/bin/python
# -*- coding: utf-8 -*-
# Test ID: test-01
# Test name: Login Test
# Expect output: Login successful
# Step description:
#      1. Open the Chrome driver;
#      2. Input the URL of test_login page;
#      3. Input the Joe as the username;
#      4. Input the password;
#      5. Choose the different company;
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import unittest, time, re, os
from webdriver_manager.chrome import ChromeDriverManager
import allure


class LoginTestJoe(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(3)
        self.base_url = "https://model.arxspan.com/test_login.asp"
        self.verificationErrors = []
        self.accept_next_alert = True

    @allure.testcase('test_login test demo')
    def test1(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Demo')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
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

    @allure.testcase('test_login test Accent Tx Model')
    def test2(self):
            driver = self.driver
            driver.get(self.base_url)
            driver.maximize_window()
            driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
            driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
            driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
            time.sleep(1)
            select = Select(driver.find_element_by_tag_name('select'))
            select.select_by_visible_text('Accent Tx Model')
            driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
            time.sleep(3)
            driver.switch_to.window(driver.window_handles[-1])
            # driver.switch_to.frame("submitFrame")
            test_value = driver.find_element_by_class_name('headUserName').text
            print(test_value)
            a = u'Joe Chemist'
            test_value2 = driver.find_element_by_class_name('companySection').text
            print(test_value2)
            b = u'Accent Tx Model'

            if a in test_value and b in test_value2:
                valid = True
            else:
                valid = False
                picture_name = 'test_3_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
                driver.get_screenshot_as_file(picture_name)
            self.assertTrue(valid)

    @allure.testcase('test_login test BIM')
    def test3(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('BIM')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Demo'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'BIM'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_4_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test CpdTrackingNoInv')
    def test4(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CpdTrackingNoInv')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CpdTrackingNoInv'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_5_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test CT DEMO')
    def test5(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('CT DEMO')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'CT DEMO'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_6_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test Formulation Demo')
    def test6(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Formulation Demo')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Formulation Demo'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_7_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test Model Test Script Company')
    def test7(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Model Test Script Company')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Model Test Script Company'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_8_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test Relay Test')
    def test8(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Relay Test')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joey Chemical'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Relay Test'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_9_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test Sunovion Model - Work Requests')
    def test9(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Sunovion Model - Work Requests')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe demo'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Sunovion Model - Work Requests'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_10_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)

    @allure.testcase('test_login test Workflow Pilot - ARV')
    def test10(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.maximize_window()
        driver.find_element_by_id('test_login-email').send_keys('joe@demo.com')
        driver.find_element_by_id('test_login-pass').send_keys('carbonCopee')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.RETURN)
        time.sleep(1)
        select = Select(driver.find_element_by_tag_name('select'))
        select.select_by_visible_text('Workflow Pilot - ARV')
        driver.find_element_by_id('test_login-submit').send_keys(Keys.ENTER)
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[-1])
        # driver.switch_to.frame("submitFrame")
        test_value = driver.find_element_by_class_name('headUserName').text
        print(test_value)
        a = u'Joe Chemist'
        test_value2 = driver.find_element_by_class_name('companySection').text
        print(test_value2)
        b = u'Workflow Pilot - ARV'

        if a in test_value and b in test_value2:
            valid = True
        else:
            valid = False
            picture_name = 'test_10_' + str(time.strftime('%Y%m%d%H%M%S')) + ' .png'
            driver.get_screenshot_as_file(picture_name)
        self.assertTrue(valid)





