# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
import pytest
login_url = "https://www.amazon.com/ap/signin?_encoding=UTF8&clientContext=15e6c219e9f9f248e18d2ae529efbd&marketplaceId=A384XSLT9ODACQ&openid.assoc_handle=amzn_mturk_worker_faster_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=43200&openid.return_to=https%3A%2F%2Fworker.mturk.com%2F%3Fend_signin%3D1"
@pytest.fixture(scope='module')
def wdriver():

        driver = webdriver.Chrome()
        driver.implicitly_wait(30)
        return driver


#
# def test0_page_has_loaded(wdriver):
#         wdriver.get(login_url)
#         delay = 30  # seconds
#         while True:
#                 try:
#                         WebDriverWait(wdriver, delay).until(
#                                 EC.presence_of_element_located(wdriver.find_element_by_xpath('//*[@id="MainContent"]/div[3]/div/div/h1')))
#                         print("Page is ready!")
#                         break  # it will break from the loop once the specific element will be present.
#                 except TimeoutException:
#                         print("Loading took too much time!-Try again")

def test_1_login(wdriver):
        wdriver.get(login_url)

        wdriver.find_element_by_id('ap_email').send_keys("nadafgouse510@gmail.com")
        wdriver.find_element_by_id('ap_password').send_keys("Nadaf@123")
        time.sleep(2)
        wdriver.find_element_by_id('signInSubmit').click()

        time.sleep(2)
        current_url = wdriver.current_url
        print(current_url)
        if 'signin' in current_url:
                time.sleep(2)
                test_1_login(wdriver)
        else:
                pass

def test_2_filter_hits(wdriver):
        worker_url = 'https://worker.mturk.com'
        wdriver.get(worker_url)
        wdriver.find_element_by_xpath('/html/body/div[2]/nav[1]/div/div[1]/div/button[3]').click()
        time.sleep(1)
        wdriver.find_element_by_xpath('//*[@id="filters[qualified]"]').click()
        time.sleep(1)
        wdriver.find_element_by_xpath('//*[@id="filters[min_reward]"]').clear()
        time.sleep(1)
        wdriver.find_element_by_xpath('//*[@id="filters[min_reward]"]').send_keys(0)
        time.sleep(1)
        wdriver.find_element_by_xpath('//*[@id="filter"]/div/div/form/div[3]/div[2]/button[2]').click()
        time.sleep(1)

def test_3_tamil_mcq(wdriver):
        wdriver.find_element_by_id('mturkSearchForm').send_keys("Tamil")
        wdriver.find_element_by_id('mturkSearchForm').send_keys(Keys.ENTER)
        time.sleep(1)
        wdriver.find_element_by_xpath('//*[contains(text(),"How would you rate this sentence?")]').click()


