<h1>Crypto Twitter Bot</h1>

To use generate api keys by creating an account with twitter developers.

The bot listens to user defined twitter ids for a mention of the top cryptocurrencies.

If a tweet contains a popular cryptocurrency that corresponds with a crypto in the crypto.txt file,
A message will be sent to Discord if a webhook url is provided.

To add or remove cryptocurriences, edit the cryptos.txt file.

To add Twitter accounts, insert the accounts Twitter ID into the emply list:
follow = []

Or

Un comment:

'''
print('Bot is listening to the following twitter accounts:')
friends =[]
for user in tweepy.Cursor(api.friends, screen_name="ubot_we_friends").items():
    print(user.screen_name)
    friends.append(str(user.id))'''


And change follow=follow to follow=friends



