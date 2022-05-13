import requests
import json
from dataset import dataset

def get_price_vs_usd(id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd'
    headers = {'content':'application/json'}
    r = requests.get(url,headers=headers)
    response = r.json()
    return response

def percent_change(ath,price):
    change = ((price-ath)/ath)*100
    return float(change)

dataset = dataset

for data in dataset:
    name = data['name']
    coin_id = data['api']
    response = get_price_vs_usd(coin_id)
    all_time_high = float(data['ath'])
    current_price = float(response[coin_id]['usd'])
    change = percent_change(all_time_high,current_price)
    if change <= -85:
        print(name, f'{round(change,2)}%')