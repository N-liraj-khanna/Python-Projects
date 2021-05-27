from twilio.rest import Client
import requests
import os

# --------------- Constants & Variables --------------- #
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCKS_API_KEY = os.environ['ALPHA_ADVANTAGE_API_KEY']
STOCKS_PARAMS = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": STOCKS_API_KEY
}

NEWS_API_KEY = os.environ['NEWS_API_KEY']
NEWS_PARAMS = {
    "qInTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}

TWILIO_ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
TWILIO_AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stocks_response = requests.get("https://www.alphavantage.co/query", params=STOCKS_PARAMS)
stocks_response.raise_for_status()
stocks_data = stocks_response.json()["Time Series (Daily)"]

stocks_data_list = [value for (key, value) in stocks_data.items()]

yesterdays_closing_price = float(stocks_data_list[1]['4. close'])
day_bfr_yesterdays_closing_price = float(stocks_data_list[0]['4. close'])

stocks_percentage = round(((yesterdays_closing_price - day_bfr_yesterdays_closing_price) /
                               yesterdays_closing_price) * 100)
if stocks_percentage >= 0:
    symbol = "🔺"
else:
    symbol = "🔻"

# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.

if abs(stocks_percentage) >= 2:
    news_response = requests.get("https://newsapi.org/v2/everything", params=NEWS_PARAMS)
    news_data = news_response.json()['articles'][:3]

# Send a separate message with the percentage change and each article's title and description to your phone number.
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)

    messages = [f"{STOCK}: {symbol}{abs(stocks_percentage)}%\nHeadline: {data['title']}\nBrief: {data['description']}"
                for data in news_data]

    for message in messages:
        client.messages.create(
            body=message,
            from_="your Verified Phone Number From Twilio",
            to="your Phone Number"
        )
