
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

import time
login_url = "https://www.amazon.com/ap/signin?_encoding=UTF8&clientContext=15e6c219e9f9f248e18d2ae529efbd&marketplaceId=A384XSLT9ODACQ&openid.assoc_handle=amzn_mturk_worker_faster_desktop_us&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.mode=checkid_setup&openid.ns.pape=http%3A%2F%2Fspecs.openid.net%2Fextensions%2Fpape%2F1.0&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&openid.pape.max_auth_age=43200&openid.return_to=https%3A%2F%2Fworker.mturk.com%2F%3Fend_signin%3D1"
worker_url = 'https://worker.mturk.com'
driver = webdriver.Chrome()
driver.implicitly_wait(15)
driver.get('worker_url')
timeout = 20
try:
    element_present = EC.presence_of_element_located((By.XPATH, '//a[@href="dashboard?ref=w_hdr_db"]'))
    WebDriverWait(driver, timeout).until(element_present)
except TimeoutException:
    print( "Timed out waiting for page to load")



# driver.get(login_url)
# driver.find_element_by_id('ap_email').send_keys("kiran.sk.sdet@gmail.com")
# driver.find_element_by_id('ap_password').send_keys("hanTZ1234")
# time.sleep(10)
# driver.find_element_by_id('signInSubmit').click()

