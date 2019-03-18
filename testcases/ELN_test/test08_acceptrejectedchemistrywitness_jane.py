# Test ID: testELN-08
# Test name: Jane has accept the chemistry biology_concept_experiments witness request by Joe Test
# Expect output:
#      1. Check received witness request from Joe is showing ;
#      2. Successful accept witness request send by Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Check the witness request is showing the notification;
#      5. Select the chemistry biology_concept_experiments name which shared by Joe;
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
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessacceptationjane')
    def test1(self):
        driver = janelogin()
        # check the witness requests is showing the notification
        driver.implicitly_wait(20)
        assert driver.find_element_by_id('witnessRequestsHolder').is_displayed()
        # select the analytical biology_concept_experiments name
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(1)')
        button.click()
        # sign and witness
        email = driver.find_elements_by_id('signEmail')[1]
        email.send_keys('jane@demo.com')
        password = driver.find_elements_by_id('password')[1]
        password.send_keys('carbonCopee')
        form = driver.find_element_by_id('witnessForm')
        form.click()
        driver.find_element_by_id('witnessSubmitButton').click()
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        assert WebDriverWait(driver, 5).until(ec.visibility_of_element_located((By.ID, "historyNavLink")))
        time.sleep(2)
        # Log out
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def janelogin():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get('https://model.arxspan.com/login.asp')
    driver.find_element_by_id('login-email').send_keys('jane@demo.com')
    driver.find_element_by_id('login-pass').send_keys('carbonCopee')
    driver.find_element_by_id('login-submit').send_keys(Keys.RETURN)
    time.sleep(1)
    select = Select(driver.find_element_by_tag_name('select'))
    select.select_by_visible_text('Model Test Script Company')
    driver.find_element_by_id('login-submit').send_keys(Keys.ENTER)
    return driver
