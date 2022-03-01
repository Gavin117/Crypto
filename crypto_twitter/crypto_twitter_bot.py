from datetime import datetime
import tweepy
import requests
import json

#Add your own api tokens by creating an app on twitter developer
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth.secure = True
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True, compression=True)


def search_tweet_for_crypto(tweet):
    
    def crypto_list():
        with open('cryptos.txt', 'r') as f:
             cryptos = f.read()
             f.close()
        x = cryptos.split(',')
        x = [i.replace('\'','') for i in x]
        x= [i.lower().strip() for i in x]
        hashtags = ['#'+i for i in x[::2]]
        cashtags = ['$'+i for i in x[1::2]]
        hashtickers = ['#'+i for i in x[1::2]]
        return x,hashtags,cashtags,hashtickers
    
    names,hashtag,cashtag, hashtick = crypto_list()
    crypto_list = name+ hashtag + cashtag + hashtick
    words = tweet.strip().split(' ')
    words = [i.lower() for i in words]
    for word in words:
        if word in crypto_list:
            return word
            break
        else:
            pass


def send_msg(author,link,message,timestamp):
        content= {
            "embeds": [
                    {
                        "title": f"Link to {author} tweet.",
                        "color":1127128,
                        "url":f"{link}",
                        "description":f"{message}",
                        "footer":{"text":"Text Here"},
                        "timestamp":f"{timestamp}"
                        }
                    ]
                }
        requests.post(webhook,json.dumps(content),headers={"Content-Type": "application/json"})
    




class MyStreamListener(tweepy.StreamListener): 
    def on_status(self, status):
            timestamp = datetime.utcnow()
            tweet = status.text
            author= status.user.screen_name
            link = f"https://twitter.com/{author}/status/{status.id}"
            if not 'RT @' in tweet:
                if str(status.user.id) in friends:
                    coin = search_tweet_for_crypto(tweet)
                    if coin == None:
                        pass
                    else:
                        message = f'{author} mentioned this coin ```{coin}``` in his latest tweet!\n\n{tweet}'
                        #send_msg(author,link,message,timestamp)         
                    
    def on_error(self, status_code):
        if status_code == 420:
            return False


print('Bot has Started!')

'''
print('Bot is listening to the following twitter accounts:')

friends =[]
for user in tweepy.Cursor(api.friends, screen_name="ubot_we_friends").items():
    print(user.screen_name)
    friends.append(str(user.id))'''

follow = [] #Input the user(s) twitter id(s) to start listening for crypto tweets.
webhook = ''#Add a discord webhook url and remove # from send_msg in MyStreamListener

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(follow=follow, is_async = True)
