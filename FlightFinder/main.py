import requests
from manage_data import DataManager
from sheets_manager import SheetsManager

FLIGHTS_API_KEY = "2kjIwVPgZh02U6iOTf8bG8xrVpkaAW9g"
FLIGHTS_ENDPOINT = "https://tequila-api.kiwi.com/"

sheets = SheetsManager()
all_cities = sheets.set_iata_codes()
