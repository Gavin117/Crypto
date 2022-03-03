import requests
import json
from datetime import date

def get_price_vs_usd(id):
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={id}&vs_currencies=usd'
    r = requests.get(url,headers=headers)
    response = r.json()
    return response


def get_trending():
    url = 'https://api.coingecko.com/api/v3/search/trending'
    r = requests.get(url,headers=headers)
    response = r.json()
    coins = response['coins']
    return coins


def parse_data(coin_list):
    btc = get_price_vs_usd('bitcoin')
    btc_usd = float(btc['bitcoin']['usd'])
    data= []
    for coin in coin_list:
        name = coin['item']['name']
        id= coin['item']['id']
        url = f'https://www.coingecko.com/en/coins/{id}'
        mc_rank = coin['item']['market_cap_rank']
        price = float(coin['item']['price_btc'])
        price_usd = round(price*btc_usd,2)
        coin_dict = {'name': name.capitalize(),'rank':mc_rank,'price_usd':price_usd,'url':url}
        data.append(coin_dict)
    return data



if(__name__=="__main__"):
  headers= {'content-Type':'application/json'}
  data = get_trending()
  trending = parse_data(data)
  for coin in trending:
    print(coin)




