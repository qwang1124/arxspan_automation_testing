# Test ID: test-01
# Test name: Jane has reject the analytical biology_concept_experiments witness request by Joe Test
# Expect output:
#      1. Check received witness request from Joe is showing ;
#      2. Add a new note;
#      3. Successful reject witness request send by Joe;
# Step description:
#      1. Open the Chrome driver;
#      2. Login Jane as the user;
#      3. Choose 'Model Test Script Company' as the company ;
#      4. Check the witness request is showing the notification;
#      5. Select the analytical biology_concept_experiments name which shared by Joe;
#      6. Add a new note;
#      7. Reject the witness request
#      8. Log out.
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessrejectionjane')
    def test1(self):
        driver = testjanelogin()
        # check the witness requests is showing the notification
        assert driver.find_element_by_id('witnessRequestsHolder').is_displayed()
        # select the analytical biology_concept_experiments name
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(2)')
        button.click()
        # add a note to reject reason
        driver.find_element_by_id('reasonBox').send_keys('TESTING')
        # reject the witness request
        driver.find_element_by_id('rejectSubmitButton').click()
        time.sleep(2)
        driver.get('https://model.arxspan.com/arxlab/dashboard.asp')
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="navMyExperiments"]/ul/li[1]/a').click()
        time.sleep(2)
        assert driver.find_element_by_id('historyNavLink').is_displayed()
        driver.find_element_by_link_text('Logout').click()
        driver.close()


def testjanelogin():
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
