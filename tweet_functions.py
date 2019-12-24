import os
import tweepy
from dotenv import load_dotenv

load_dotenv()


def setup_api():
    auth = tweepy.OAuthHandler(os.getenv('CONSUMER_KEY'), os.getenv('CONSUMER_SECRET'))
    auth.set_access_token(os.getenv('ACCESS_TOKEN'), os.getenv('ACCESS_TOKEN_SECRET'))
    return tweepy.API(auth)


def post_tweet(content):
    api = setup_api()
    return api.update_status(status=content)


def get_last_tweet():
    api = setup_api()
    timeline = api.user_timeline(count=1)
    if timeline:
        return timeline[0].text
    return None
