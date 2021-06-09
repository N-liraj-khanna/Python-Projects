import os
import time

from selenium import webdriver

WEB_DRIVER_PATH = 'C:/Program Files (x86)/WebDriver/geckodriver.exe'

driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH)

driver.get('https://tinder.com/')

MY_EMAIL = os.environ['EMAIL']
MY_PASSWORD = os.environ['PASS']

time.sleep(2)
driver.find_element_by_css_selector('a.button').click()

time.sleep(2)
options = driver.find_element_by_css_selector('button.Td\(u\)')
if options.text == 'MORE OPTIONS':
    options.click()
    time.sleep(1)

driver.find_element_by_xpath('/html/body/div[2]/div/div/div[1]/div/div[3]/span/div[2]/button').click()

time.sleep(2)
driver.switch_to.window(driver.window_handles[-1])

driver.find_element_by_css_selector('#email').send_keys(MY_EMAIL)
driver.find_element_by_css_selector('#pass').send_keys(MY_PASSWORD)
driver.find_element_by_name('login').click()

time.sleep(3)
driver.switch_to.window(driver.window_handles[-1])

time.sleep(1)
driver.find_element_by_css_selector('button.Ell:nth-child(1)').click()
time.sleep(8)  # wait for the user to allow location access

driver.find_element_by_css_selector('button.button:nth-child(2)').click()
time.sleep(5)  # wait for the user to allow location access (again)

for _ in range(0, 500):
    print(_)
    driver.find_element_by_css_selector('div.Mx\(a\):nth-child(4) > button:nth-child(1)').click()
