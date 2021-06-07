import time
import os
from selenium import webdriver
# from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

WEB_DRIVER_PATH = 'C:\Program Files (x86)\WebDriver/geckodriver.exe'
LINKEDIN_URL = 'https://www.linkedin.com/'

driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH)
driver.get(LINKEDIN_URL)

MY_EMAIL = os.environ['EMAIL']
MY_PASS = os.environ['PASS']

driver.find_element_by_link_text('Sign in').click()

time.sleep(3)
email = driver.find_element_by_name('session_key')
email.send_keys(MY_EMAIL)
password = driver.find_element_by_name('session_password')
password.send_keys(MY_PASS)
driver.find_element_by_css_selector('.login__form_action_container button').click()

time.sleep(3)
jobs_tab = driver.find_elements_by_css_selector('.global-nav__primary-item a')
for jobs in jobs_tab:
    if jobs.get_attribute('data-link-to') == 'jobs':
        jobs.click()
        break

time.sleep(3)
title = driver.find_element_by_css_selector('.jobs-search-box__keyboard-text-input')
title.send_keys(input('What are you Looking for?  '))
location = driver.find_element_by_css_selector('.jobs-search-box__input--location input')
location.send_keys('Worldwide')
title.send_keys(Keys.RETURN)

time.sleep(3)
for filters in driver.find_elements_by_css_selector('#search-reusables__filters-bar button')[1:]:
    if filters.get_attribute('aria-label') == 'Remote filter.' or \
            filters.get_attribute('aria-label') == 'Easy Apply filter.':
        filters.click()

time.sleep(3)
jobs_li = driver.find_elements_by_class_name('job-card-list__title')
for job in jobs_li:

    time.sleep(1)
    try:
        for button in driver.find_elements_by_css_selector('.jobs-s-apply button'):
            button.click()
            time.sleep(3)
    except:
        continue

    # number (if number not inbuilt)
    # try:
    #     for num in driver.find_elements_by_css_selector('.fb-single-line-text input'):
    #         num.send_keys('147852369')
    #     driver.find_element_by_css_selector('footer button').click()
    #     time.sleep(3)
    # except:
    #     pass

    # resume
    try:
        driver.find_element_by_css_selector('footer .artdeco-button--primary').click()
        time.sleep(3)
    except:
        pass

    # review
    try:
        for years_of_exp in driver.find_elements_by_css_selector('.fb-single-line-text input'):
            years_of_exp.send_keys('1')
        driver.find_element_by_css_selector('footer .artdeco-button--primary').click()
        time.sleep(3)
    except:
        pass

    # Apply now or later
    try:
        for radio_button in driver.find_elements_by_css_selector('.fb-radio-buttons .fb-radio label'):
            radio_button.click()
        driver.find_element_by_css_selector('footer .artdeco-button--primary').click()
        time.sleep(3)
    except:
        pass

    try:
        driver.find_element_by_css_selector('.justify-flex-end .artdeco-button--primary').click()
        time.sleep(3)
    except:
        pass

    try:
        driver.find_element_by_css_selector('.artdeco-button__icon').click()
        time.sleep(3)
    except:
        pass

    job.click()

driver.quit()
