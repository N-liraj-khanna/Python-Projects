import requests

SHEETS_ENDPOINT = "https://api.sheety.co/8e7a7d1cc3512b560de163312ecb220c/flightDeals/prices"
SHEETS_TOKEN = "idkyubutiamfinejustleaveme"

FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com"
FLIGHTS_API_KEY = "2kjIwVPgZh02U6iOTf8bG8xrVpkaAW9g"


class SheetsManager:
    def __init__(self):
        self.sheets_headers = {
            "Authorization": f"Bearer {SHEETS_TOKEN}"
        }
        self.flights_headers = {
            "apikey": FLIGHTS_API_KEY
        }
        self.sheets_response = requests.get(url=SHEETS_ENDPOINT, headers=self.sheets_headers)
        self.sheets_response.raise_for_status()
        self.sheets_data = self.sheets_response.json()['prices']

    def get_destination_code(self, location):
        params = {
            "term": location
        }
        location_response = requests.get(url=f"{FLIGHTS_ENDPOINT}/locations/query",
                                          params=params, headers=self.flights_headers)
        iata_code = location_response.json()['locations'][0]['code']
        return iata_code

    def set_iata_codes(self):
        for city in self.sheets_data:
            params = {
                "price": {
                    "iataCode": self.get_destination_code(city['city'])
                }
            }
            response = requests.put(url=f"{SHEETS_ENDPOINT}/{city['id']}",
                                                headers=self.sheets_headers, json=params)
            response.raise_for_status()
