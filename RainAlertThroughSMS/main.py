import requests
from twilio.rest import Client


# ------------------- Constants & Global Variables ------------------- #

# Open Weather Map API
WEATHER_MAP_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = "your Api Key Of Open weather map"

MY_LAT = "yourLatitude"
MY_LONG = "yourLongitude"


# Twilio API
ACCOUNT_SID = "your twilio account sid"
AUTH_TOKEN = "your twilio account auth token"

# Parameters for the Endpoint in OWM API
params = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude": "current,daily,minutely,alerts",
    "appid": API_KEY
}

# ------------------- API Data Config ------------------- #

response = requests.get(WEATHER_MAP_ENDPOINT, params=params)
response.raise_for_status()
weather_data = response.json()

will_rain = False

for data in weather_data['hourly'][:12]:
    weather_id = data['weather'][0]['id']
    if weather_id < 700:
        will_rain = True
        break

if will_rain:

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages.create(
        body="It Definitely will Rain today. Make sure to bring an Umbrella ☂️.",
        from_='your generate phone number from twilio',
        to='sender phone number(verified only)'
    )
    print(message.status)


