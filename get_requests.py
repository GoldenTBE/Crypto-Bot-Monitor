import requests
import json
from Keys import Nomics_api


def get_crypto_data(crypto):
    url = "https://api.nomics.com/v1/currencies/ticker?key=" + Nomics_api + "&ids="+ crypto +"&interval=1h,1d&per-page=100&page=1"
    r = requests.get(url) #get_request to API 
    resp_json = json.loads(r.text) #conver to python dict.
    if r.status_code != 200: #200 == good request; tests for bad request, discord bot handles error
        raise RuntimeError 
    x = json.dumps(resp_json, indent=2)
    print(x) #easier to read API response for dev.

    
    all_time_high = (resp_json[0]['high']) #all time high
    all_time_high_date = (resp_json[0]['high_timestamp'])

    data = { #returning dict, should be easier when embedding in discord bot - O(1)
        "price" :(resp_json[0]['price']) + ' USD', #current_price
        "picture" : (resp_json[0]['logo_url']), #image for discord_bot
        "market_cap" : (resp_json[0]['market_cap']), #market_cap 
        "all_time_high" : (resp_json[0]['high']), #all time high
        "all_time_high_date" : (resp_json[0]['high_timestamp']), #date of all time high 
        "high_with_date" : (all_time_high + ' @ ' + all_time_high_date[:10]),
        "change_1hr" : (resp_json[0]['1h']['price_change']), #price change within 1hr
        "change_1d" : (resp_json[0]['1d']['price_change']) #price change within 1d
    }

    return data

def all_crypto_prices(): #future
    pass


if __name__ == "__main__":
    pass