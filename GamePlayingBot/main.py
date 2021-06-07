import time
from selenium import webdriver

WEB_DRIVER_PATH = "YOUR WEBDRIVER PATH"

driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH)

driver.get('http://orteil.dashnet.org/experiments/cookie/')

five_interval = time.time() + 5
timeout = time.time() + (5 * 60)

cookie = driver.find_element_by_id('cookie')

extra_items = driver.find_elements_by_css_selector('#store div')
extra_items.pop()
extra_ids = [extra.get_attribute('id') for extra in extra_items]

while True:
    cookie.click()
    if time.time() >= timeout:
        print(driver.find_element_by_id('cps').text)
        break

    if time.time() >= five_interval:
        five_interval += 5

        extra_items_prices = driver.find_elements_by_css_selector('#store b')
        extra_items_prices.pop()
        extra_items_as_int = [int(extra.text.split(' - ')[1].replace(',', '')) for extra in extra_items_prices]

        for idx in range(len(extra_ids) - 1, -1, -1):
            if extra_items_as_int[idx] <= int(driver.find_element_by_id('money').text):
                driver.find_element_by_id(extra_ids[idx]).click()
                break

driver.quit()
