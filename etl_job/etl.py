import time
import pymongo
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

"""posgresql connection"""
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")


s  = SentimentIntensityAnalyzer()
# Establish a connection to the MongoDB server
client = pymongo.MongoClient(host="mongodb", port=27017)

time.sleep(10)  # seconds
# Select the database you want to use withing the MongoDB server

db = client.twitterdb

pg = create_engine(f'postgresql://{USER}:{PASSWORD}@postgresdb:5432/twitterdb', echo=True)

pg.execute("""
    CREATE TABLE IF NOT EXISTS tweets (
    text VARCHAR(500),
    sentiment NUMERIC );""")
while True:
    docs = db.tweets.find(limit=5)
    for doc in docs:
        text = doc['text']
        sentiment = s.polarity_scores(doc['text'])
        print(sentiment)
        score = sentiment['compound']
        query = "INSERT INTO tweets VALUES (%s, %s);"
        pg.execute(query, (text, score))
        print(doc)
    time.sleep(3600)

