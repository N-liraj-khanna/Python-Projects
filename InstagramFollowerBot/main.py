import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys

WEB_PATH = 'C:/Program Files (x86)/WebDriver/geckodriver.exe'

driver = webdriver.Firefox(executable_path=WEB_PATH)
driver.get('https://www.instagram.com')

USERNAME = "YOUR EMAIL"
PASS = 'YOUR PASS'

time.sleep(2)
driver.find_element_by_name('username').send_keys(USERNAME)
driver.find_element_by_name('password').send_keys(PASS)
driver.find_element_by_css_selector('#loginForm > div > div:nth-child(3) > button > div').click()

time.sleep(5)
driver.find_element_by_css_selector('.XTCLo').send_keys('food')

time.sleep(3)
for account in driver.find_elements_by_css_selector('.fuqBx a'):
account.click()

driver.find_elements_by_css_selector('.fuqBx a')[3].click()

time.sleep(3)
driver.find_element_by_css_selector('li.Y8-fY:nth-child(2) > a:nth-child(1)').click()

time.sleep(5)
driver.find_element_by_css_selector('.PZuss > li:nth-child(1)').click()

i = 0
while True:
    try:
        driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
    except NoSuchElementException:
        pass
    try:
        for follower in driver.find_elements_by_css_selector('li .y3zKF')[i:6]:
            follower.click()
            time.sleep(.5)
    except ElementClickInterceptedException:
        pass

    i += 1
    driver.execute_script("window.scrollTo(0, 50)")

while True:
    if len(followers) != 0:
        break
    followers = driver.find_elements_by_css_selector('li .y3zKF')
    driver.find_element_by_css_selector("body").send_keys(Keys.DOWN)

i = 1
for follower in followers:
    try:
        driver.find_element_by_css_selector('button.aOOlW:nth-child(2)').click()
    except NoSuchElementException:
        pass
    while True:
        if len(followers) != 0:
            break
        followers = driver.find_elements_by_css_selector('li .y3zKF')
        driver.find_element_by_css_selector("body").send_keys(Keys.DOWN)
    follower.click()
    print(i)
    if i >= 6:
        driver.find_element_by_css_selector("body").send_keys(Keys.DOWN)
    i += 1
    time.sleep(1)
