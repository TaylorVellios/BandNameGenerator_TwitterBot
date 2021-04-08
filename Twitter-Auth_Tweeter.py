# ReallyGr8BandNames
import random
from datetime import date, datetime
import tweepy
import webbrowser


import sched, time
s = sched.scheduler(time.time, time.sleep)

from config import api_key, api_secret, bearer_token
import bandnamegen

#Twitter Stuff
twitter_callback = 'oob'
auth = tweepy.OAuthHandler(api_key, api_secret, twitter_callback)
redirect_url = auth.get_authorization_url()

login = True
while login:
    webbrowser.open(redirect_url)
    print()
    user_pin = input('Enter the Pin from the Twitter Auth Pop-Up: ')
    print()
    try:
        auth.get_access_token(user_pin)
        print()
        print('Tokens Confirmed')
        login = False
    except:
        print('Pin Number INVALID. Please Try Again\n')

api = tweepy.API(auth)
me = api.me()
print(f'Confirming Tokens for user: {me.screen_name}\n'
        f'Access Token: {auth.access_token}\n'
        f'Access Token Secret: {auth.access_token_secret}\n')

divider = '--------------------------------------------------------------'
print(divider)


def get_name_and_tweet():
    right_now = datetime.now()
    output = random.choice(bandnamegen.make_name_1())

    band_name = output[0]
    genre = output[1]

    tweet_string = ''
    if genre[0].upper() in 'AEIOU':
        tweet_string = f'For an {genre}:\n{band_name}'
    else:
        tweet_string = f'For a {genre}:\n{band_name}'

    print(f'Tweeting at {right_now}: \n{tweet_string}')
    api.update_status(tweet_string)
    print(divider)
    s.enter(7400,1, get_name_and_tweet)


s.enter(1,1, get_name_and_tweet)
s.run()

s.cancel()