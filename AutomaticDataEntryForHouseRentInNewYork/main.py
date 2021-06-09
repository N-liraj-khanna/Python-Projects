import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

ZILLOW_URL = 'https://www.zillow.com'
G_FORMS_URL = 'YOUR G FORMS LINK'

CITY = 'New York'
WEB_DRIVER_PATH = 'WEB DRIVER PATH'

driver = webdriver.Firefox(executable_path=WEB_DRIVER_PATH)
driver.get(ZILLOW_URL)

driver.find_element_by_css_selector('#search-box-input').send_keys(CITY)
time.sleep(1)
driver.find_element_by_css_selector('#search-box-input').send_keys(Keys.BACKSPACE)
time.sleep(2)
driver.find_element_by_css_selector('#react-autowhatever-1--item-0 > div:nth-child(1) > div:nth-child(1)').click()

driver.find_element_by_css_selector('.sc-14dvu6m-2 > li:nth-child(2) > button:nth-child(1)').click()
time.sleep(1)

driver.find_element_by_css_selector('#price').click()
time.sleep(.5)
driver.find_element_by_css_selector('#price-exposed-min').click()
driver.find_element_by_css_selector('#min-600 > button:nth-child(1)').click()
time.sleep(.5)
driver.find_element_by_css_selector('#price-exposed-max').click()
driver.find_element_by_css_selector('#max-2000 > button:nth-child(1)').click()
time.sleep(1)

driver.find_element_by_css_selector('#beds').click()
driver.find_element_by_css_selector('.NxaZL > button:nth-child(2)').click()
driver.find_element_by_css_selector('.popover-visible > div:nth-child(2) > div:nth-child(2) > button:nth-child(1)')\
                                    .click()

time.sleep(1)
driver.find_element_by_css_selector('#sort-popover').click()
driver.find_element_by_css_selector('button.StyledMenuItem-c11n-8-37-0__sc-1blp609-0:nth-child(3)').click()

articles_list = []
articles_count = 0

page_num = 1

while True:
    time.sleep(5)
    driver.find_element_by_css_selector('.search-title').click()

    for _ in range(85):
        driver.find_element_by_css_selector('body').send_keys(Keys.DOWN)
        time.sleep(.1)

    all_articles = driver.find_elements_by_css_selector('.photo-cards li article')

    for article in all_articles:
        address = article.find_element_by_css_selector('.list-card-addr').text
        price = article.find_element_by_css_selector('.list-card-price').text
        link = article.find_element_by_css_selector('.list-card-link').get_attribute('href')

        articles_list.append({
            'address': address,
            'price': price,
            'link': link
        })
        articles_count += 1

        print(articles_count)
        if articles_count == 100:
            break

    if articles_count == 100:
        break

    time.sleep(2)

    pages = driver.find_elements_by_css_selector('.ekGcXR')

    if page_num >= len(pages):
        break
    pages[page_num].click()
    if page_num < 5:
        page_num += 1


time.sleep(2)

# G forms part
driver.get(G_FORMS_URL)

for article in articles_list:  # Your google sheet's selectors
    driver.find_element_by_css_selector('ADDRESS FIELD').send_keys(article['address'])
    driver.find_element_by_css_selector('PRICE FIELD').send_keys(article['price'])
    driver.find_element_by_css_selector('LINK FIELD').send_keys(article['link'])
    driver.find_element_by_css_selector('BUTTON selector').click()
    driver.find_element_by_link_text('Submit another response').click()
