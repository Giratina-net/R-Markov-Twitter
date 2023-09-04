
import tweepy
import requests
import json
from os import getenv

api_key=getenv("API_KEY")
api_secret_key=getenv("API_SECRET_KEY")
access_token=getenv("ACCESS_TOKEN")
access_secret_token=getenv("ACCESS_SECRET_TOKEN")
bearer_token=getenv("BEARER_TOKEN")
client = tweepy.Client(consumer_key=api_key, consumer_secret=api_secret_key, bearer_token=bearer_token, access_token=access_token, access_token_secret=access_secret_token)
auth = tweepy.OAuthHandler(consumer_key=api_key, consumer_secret=api_secret_key)
auth.set_access_token(key=access_token, secret=access_secret_token)

def generate_tweet():
    tweet=json.loads(requests.get('https://api.giratina.net/v1/raika').text)['text']
    return tweet

def run():
    client.create_tweet(text=generate_tweet())

if __name__ == '__main__':
    run()

print("start")
