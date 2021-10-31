import requests
import json
import os
from requests.models import Response
from data_handler import change_to_price
from dotenv import load_dotenv

load_dotenv()
Nomics_api = os.getenv("Nomics_api")

def get_crypto_data(crypto):
    url = "https://api.nomics.com/v1/currencies/ticker?key=" + Nomics_api + "&ids="+ crypto +"&interval=1h,1d,7d,30d&per-page=100&page=1"
    r = requests.get(url) #get_request to API 
    if r.status_code != 200: #200 == good request; tests for bad request, discord bot handles error
        raise RuntimeError 
    #x = json.dumps(resp_json, indent=2)
    #print(x) #easier to read API response for dev.
    resp_json = json.loads(r.text) #conver to python dict. 
    response = resp_json[0] 
    
    all_time_high = (response['high']) 
    all_time_high_date = (response['high_timestamp'])

    dates_needed = ['1h','1d','7d','30d']
    price = []
    for i in dates_needed:
        price.append(change_to_price(response['price'],response[i]['price_change']))

    

    data = { #returning dict, should be easier when embedding in discord bot - O(1)
        "Current Price" :(resp_json[0]['price']), #current_price
        "All Time High" : (all_time_high[:6] + ' @ ' + all_time_high_date[:10]),
        "Price 1 Hour ago" : (price[0]), #price change within 1hr
        "Price 1 Day ago" : (price[1]), #price change within 1d
        "Price 7 Days ago" : (price[2]), #price change within 7d
        "Price 30 Day ago" : (price[3]), #price change within 30d
    }

    return data

def all_crypto_prices(): 
    cryptocurrencies = 'BTC,ETH,ADA,SOL,DOGE,LTC,SHIB'
    url = "https://api.nomics.com/v1/currencies/ticker?key=" + Nomics_api + "&ids="+ cryptocurrencies 
    r = requests.get(url) 
    resp_json = json.loads(r.text)   
    data = {}
    for i in range(7):
        data[resp_json[i]['name'] + ' Price'] = resp_json[i]['price'] 
    return data


if __name__ == "__main__":
    pass