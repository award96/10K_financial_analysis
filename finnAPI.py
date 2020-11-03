import requests
import time

"""
    handle api requests
"""

API_KEY_PATH = "api.txt"
def get_api_key():

    with open(API_KEY_PATH,'r') as file:
        api_key_raw = file.readline()
        if "\n" in api_key_raw:
            api_key = api_key_raw.replace("\n","")
        else:
            api_key = api_key_raw
        return api_key

API_KEY = get_api_key()

def handle_response(response, callback_function, symbol):
    try:
        json_resp = response.json()
    except Exception as e:
        print(f"\n\n{e}")
        print(f"r:\n{response}")
        print("if 429 response, rate limit exceeded, the script will proceed in 1 minute\nIf other response, recommended to stop script")
        time.sleep(60)
        json_resp = callback_function(symbol)
    return json_resp
    
def get_tenK_json(symbol):
    r = requests.get(f'https://finnhub.io/api/v1/stock/financials-reported?symbol={symbol}&token={API_KEY}')
    return handle_response(r, get_tenK_json, symbol)

def get_profile_json(symbol):
    r = requests.get(f'https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token={API_KEY}')
    return handle_response(r, get_profile_json, symbol)
