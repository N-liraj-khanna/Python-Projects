import os
import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

WEB_DRIVER_PATH = 'YOUR WEB DRIVER PATH'

EMAIL = os.environ['EMAIL']
PASS = os.environ['PASS']

driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH)

driver.get('https://www.speedtest.net/')

time.sleep(2)
driver.find_element_by_class_name('js-start-test').click()

time.sleep(40)
while True:
    try:
        down = driver.find_element_by_class_name('download-speed').text
        up = driver.find_element_by_class_name('upload-speed').text
        break
    except NoSuchElementException:
        pass

time.sleep(5)
driver.get('https://twitter.com/')

time.sleep(2)
driver.find_element_by_xpath('/html/body/div/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div').click()
time.sleep(1)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input').send_keys(EMAIL)
driver.find_element_by_xpath(
    '/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input').send_keys(PASS)
driver.find_element_by_xpath('/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div').click()

time.sleep(5)
message = 'Hey Internet Provider, why is my internet speed ' + down + 'down/' + up + \
          'up when i pay for 100down/40up?'
driver.find_element_by_class_name('notranslate').send_keys(message)
driver.find_element_by_css_selector('div.r-urgr8i:nth-child(4) > div:nth-child(1)').click()

driver.quit()

