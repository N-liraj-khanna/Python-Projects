import datetime as dt
import requests
import smtplib
import time

# Credentials
my_email = "yourMail@mail.com"
password = "yourPassword"


# ISS Location Part
def get_iss_location():
    iss_location_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_location_response.raise_for_status()
    iss_data = iss_location_response.json()

    iss_lat = float(iss_data['iss_position']['latitude'])
    iss_lng = float(iss_data['iss_position']['longitude'])

    return iss_lat, iss_lng


# My Location Part
LAT = 13.041663999999999  # your latitude
LONG = 80.19968  # your longitude

parameters = {
    "lat": LAT,
    "lng": LONG,
    "formatted": 0  # for 24hour format
}
my_location_response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)

my_location_response.raise_for_status()
# extracting hour alone
sunrise = int(my_location_response.json()['results']['sunrise'].split('T')[1].split(':')[0])
sunset = int(my_location_response.json()['results']['sunset'].split('T')[1].split(':')[0])


def iss_location_check():
    iss_loc = get_iss_location()
    curr_hour = dt.datetime.now().hour

    if LAT + 5 >= iss_loc[0] >= LAT - 5 and \
            LONG + 5 >= iss_loc[1] >= LONG - 5 and \
            sunset <= curr_hour or curr_hour <= sunrise:
        return True


while True:
    time.sleep(60)
    if iss_location_check():
        # Establishing connection
        with smtplib.SMTP(host="smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="senderMail@mail.com",
                msg="Subject: Hey\n\nLook Up, There is a ISS up in the SKY"
            )
