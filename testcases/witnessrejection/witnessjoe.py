import time
import unittest


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import allure


class TestWitnessJane(unittest.TestCase):

    @allure.testcase('witnessrejectionjoe')
    def test1(self):
        driver = testjoelogin()
        # self.assertIn('Rejection', driver.find_element_by_class_name('notificationBodyTitle').text)
        driver.find_element_by_xpath('//*[@id="witnessRequestsHolder"]/div/div[2]/table/tbody/tr[1]/td[2]/a').click()
        button = driver.find_element_by_css_selector('#witnessButtons > a:nth-child(1)')
        button.click()
        # email = driver.find_element_by_id('signEmail')
        # driver.execute_script("arguments[0].click();", email)
        driver.find_element_by_id('signEmail').setAttribute("value", "joe@demo.com")

        driver.execute_script("document.getElementById('password').value = 'carbonCopee';")
        driver.find_element_by_class_name('css-label checkboxLabel').click()
        driver.find_element_by_id('witnessSubmitButton').click()

        driver.get('https://model.arxspan.com/arxlab/experiment_no_chemdraw.asp?id=235309')
        driver.find_element_by_id('noteTable_tab').click()
        driver.find_element_by_css_selector('#note_68272_tr > td:nth-child(1) > a').click()
        self.assertIn('TESTING', driver.find_element_by_id('note_68272_description').text)
        driver.find_element_by_id('addNoteButton').click()
        text = driver.find_element_by_id('cke_250_contents')
        driver.execute_script("arguments[0].innerHTML = 'TESTING TESTING'", text)
        button = driver.find_element_by_css_selector('#note_p_1664 > div.attachmentTableButtons > a:nth-child(1)')
        button.submit()
        driver.find_element_by_id('signExperimentButton').click()
        select = Select(driver.find_element_by_id('requesteeIdBox'))
        select.select_by_visible_text('Jane Biologist')
        driver.find_element_by_class_name('css-label checkboxLabel').click()
        # witness failed because experiment need review
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

