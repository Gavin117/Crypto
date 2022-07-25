import requests
import json
from datetime import datetime, date
from howrare import Drops, Floor

def post_discord(description):
    webhook = ''
    content = {
    "embeds": [
        {
        "title": 'Solana NFT Drops',
        "url": 'https://howrare.is/drops',
        "description": description,
        "color": 15258703,
        }
    ]
    }
    requests.post(webhook, json.dumps(content), headers={"Content-Type": "application/json"})


def parse_drops(): 
    today = date.today()
    with open('drops.json','r') as file:
        data = json.load(file)
        file.close()

    todays_drops = data['result']['data'][str(today)]
    time_utc = str(datetime.utcnow()).replace(':','')[11:15]
    #print(time_utc)

    drops_to_post = ''

    for drop in todays_drops:
        drop_time = drop['time'].replace(':','')[:4]
        time_remaining = (int(drop_time) - int(time_utc))

        #if time_remaining in range(0,101):
        if time_remaining < 0:
            drop_time = str(int(drop_time) +100)
            adjusted_time = f'{drop_time[:2]}:{drop_time[2:]} GMT'
            name = drop['name']
            price = drop['price']
            nft_img = drop['image']
            website = drop['website']
            twitter = drop['twitter']
            discord = drop['discord']
            description = drop['extra']
            drops_to_post += f'[{name}]({website}) : {price} @ {adjusted_time}\n'

    return drops_to_post





if __name__=="__main__":
    Drops()
    Floor()
    drops = parse_drops()
    post_discord(drops)