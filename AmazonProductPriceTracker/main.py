import os

import requests
import smtplib
from bs4 import BeautifulSoup

AMAZON_URL = 'https://www.amazon.in/Samsung-Galaxy-Storage-Additional-Exchange/dp/B089MSZDR7/ref=sr_1_1?crid=1RVM1QAEGUKHM&dchild=1&keywords=samsung+note+20%2B&qid=1622890485&sprefix=samsung+note%2Caps%2C324&sr=8-1'
MIN_PRICE = 60000

headers = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": os.environ['browser_data']
}


response = requests.get(url=AMAZON_URL, headers=headers)

soup = BeautifulSoup(response.text, 'lxml')

price = int(soup.find(class_='priceBlockBuyingPriceString').string.split('₹')[1].replace(',', '').strip().split('.')[0])

if price < MIN_PRICE:
    my_email = os.environ['email']
    my_password = os.environ['password']
    message = "Subject: Yo! Check out! \n\nPrice drop to 60k in amazon for Samsung Galaxy Note 10plus. Link->\n"+AMAZON_URL
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email, to_addrs=os.environ['sender_email'], msg=message)
        print(message)

