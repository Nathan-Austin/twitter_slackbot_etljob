import tweepy
import os
from dotenv import load_dotenv
import pymongo
import time
load_dotenv()

client = pymongo.MongoClient(host="mongodb", port=27017)
db = client.twitterdb


BEARER_TOKEN = os.getenv('BEARER_TOKEN')


client = tweepy.Client(
    bearer_token=BEARER_TOKEN,
    wait_on_rate_limit=True,
)


response = client.get_user(
    username='allblacks',
    user_fields=['created_at', 'description', 'location',
                 'public_metrics', 'profile_image_url']
)

user = response.data

print(dict(user))



cursor = tweepy.Paginator(
    method=client.get_users_tweets,
    id=user.id,
    exclude=['replies', 'retweets'],
    tweet_fields=['author_id', 'created_at', 'public_metrics']
).flatten(limit=20)

for tweet in cursor:
    print(tweet.text)



while True:
    search_query = "allblacks -is:retweet -is:reply -is:quote lang:en -has:links"

    cursor = tweepy.Paginator(
        method=client.search_recent_tweets,
        query=search_query,
        tweet_fields=['author_id', 'created_at', 'public_metrics'],
    ).flatten(limit=20)

    for tweet in cursor:
        db.tweets.insert_one(dict(tweet))
        print(tweet.text+'\n')
    time.sleep(3600)