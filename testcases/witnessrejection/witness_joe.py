import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessjoe')
    def test1(self):
        driver = testjoelogin()
        # self.assertIn('Rejection', driver.find_element_by_class_name('notificationBodyTitle').text)
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(1)')
        button.click()
        email = driver.find_elements_by_id('signEmail')[1]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[1]
        password.send_keys('carbonCopee')
        form = driver.find_element_by_id('witnessForm')
        form.click()
        driver.find_element_by_id('witnessSubmitButton').click()
        time.sleep(2)
        assert driver.find_element_by_id('historyNavLink').is_displayed()

    @allure.testcase('witnessrejectionjoe')
    def test1(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235309')
        driver.find_element_by_id('noteTable_tab').click()
        driver.find_element_by_css_selector('#note_68272_tr > td:nth-child(1) > a').click()
        self.assertIn('TESTING', driver.find_element_by_css_selector('#note_68272 > p:nth-child(5)').text)
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_element_by_id('cke_250_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#submitRow > a:nth-child(1)')
        button.send_keys(Keys.ENTER)

    def test3(self):
        driver = testjoelogin()
        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235309')
        time.sleep(1)
        driver.find_element_by_id('signExperimentButton').click()
        time.sleep(1)
        email = driver.find_elements_by_id('signEmail')[0]
        email.send_keys('joe@demo.com')
        password = driver.find_elements_by_id('password')[0]
        password.send_keys('carbonCopee')
        checkbox = driver.find_element_by_css_selector('#signDiv > form > section.bottomDisclaimer > div > label')
        checkbox.click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_css_selector('#signDivButtons > button:nth-child(1)').click()
        driver.find_element_by_link_text('Logout').click()
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

