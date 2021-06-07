import os
import requests
import datetime as dt


EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2"
SHEETS_ENDPOINT = os.getenv('SHEET_ENDPOINT')

NUTRITIONIX_API_KEY = os.getenv('API_KEY')
NUTRITIONIX_APP_ID = os.getenv('APP_ID')
x_user_jwt = os.getenv('X_USER_JWT')

SHEETS_AUTH_BEARER = os.getenv('SHEETS_AUTH_BEARER')

# Create Account ( Or get Account refer docs) to get the "x-user-jwt"
# AUTH_PARAMS = {
#     "password": "your password",
#     "email": "your mail",
#     "first_name": "your name",
#     "timezone": "your zone",
#     "ref": "null"
# }
# response = requests.post(url=f"{EXERCISE_ENDPOINT}/auth/signup", json=AUTH_PARAMS)

headers = {
    "x-user-jwt": x_user_jwt
}

gender = input("What is your sex? ")
weight = input("What is your weight is Kg? ")
height = input("What is your Height is Cm? ")
age = input("What is your Age? ")


EXERCISE_PARAMS = {
    "query": input("What all you did!? "),
    "gender": gender,
    "weight_kg": weight,
    "height_cm": height,
    "age": age
}

response = requests.post(url=f"{EXERCISE_ENDPOINT}/natural/exercise", json=EXERCISE_PARAMS, headers=headers)

input_data = response.json()['exercises']

print(input_data)
curr_date = dt.datetime.now().strftime("%d/%m/%Y")
curr_time = dt.datetime.now().strftime("%H:%M:%S")

headers = {"Authorization": f"Bearer {SHEETS_AUTH_BEARER}"}


for data in input_data:
    data_from_user = {
        "workout": {
            "date": curr_date,
            "time": curr_time,
            "exercise": data['name'],
            "duration": str(data['duration_min']),
            "calories": str(data['nf_calories'])
        }
    }
    sheets_response = requests.post(url=f"{SHEETS_ENDPOINT}", json=data_from_user, headers=headers)
    print(sheets_response.text)
