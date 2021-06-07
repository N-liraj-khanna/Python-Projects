import requests
import datetime as dt

PIXELA_TOKEN = "your pixela token"
PIXELA_USERNAME = "your pixela username"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

ACCOUNT_CREATE_PARAMS = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Created, and then commented it out (run only once, cuz already created)
# response = requests.post(url=PIXELA_ENDPOINT, json=ACCOUNT_CREATE_PARAMS)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{PIXELA_USERNAME}/graphs"

GRAPH_ID = "your graoh id"

GRAPH_CREATE_PARAMS = {
    "id": GRAPH_ID,
    "name": "Your Graph Name",
    "unit": "Hrs",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

# Created, and then commented it out (run only once, cuz already created)
# response = requests.post(url=GRAPH_ENDPOINT, json=GRAPH_CREATE_PARAMS, headers=graph_headers)

POST_PIXEL_ENDPOINT = f"{GRAPH_ENDPOINT}/{GRAPH_ID}"
POST_PIXEL_PARAMS = {
    "date": str((dt.date.today() - dt.timedelta(5)).strftime("%Y%m%d")),
    "quantity": "10"
}

# Posted, and then commented it out (run only once, cuz already created)
# response = requests.post(url=POST_PIXEL_ENDPOINT, json=POST_PIXEL_PARAMS, headers=headers)

UPDATE_QUANTITY = {
    "quantity": "10"
    # "color": "momiji"
}
# Updated, and then commented it out (run only once, cuz already created)
# response = requests.put(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/20210527", json=UPDATE_QUANTITY, headers=headers)


# Deleted, and then commented it out (run only once, cuz already created)
# response = requests.delete(url=f"{GRAPH_ENDPOINT}/{GRAPH_ID}/20210527", headers=headers)
# print(response.text)

# Uncomment the required things and use it :)
