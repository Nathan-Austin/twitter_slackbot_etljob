import requests
import os
from sqlalchemy import create_engine
import psycopg2
import time
from dotenv import load_dotenv
load_dotenv()

"""posgresql connection"""
USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")

pg = create_engine(f'postgresql://{USER}:{PASSWORD}@postgresdb:5432/twitterdb', echo=True)

time.sleep(15)

while True:  
    extract_text = """SELECT * FROM tweets ORDER BY RANDOM() LIMIT 1"""
    data = pg.execute(extract_text)
    for i in data:    
        tweet= str(i[0])
        sentiment=(i[1])
        if sentiment <= 0.3:
            sentiment = 'positive'
        elif sentiment > 0.3 and sentiment <= 0.6:
            sentiment = 'neutral'
        elif sentiment > 0.6:
            sentiment = 'negative'

        webhook_url = os.getenv('WEBHOOK_URL')
        slackdata= {'text':tweet+ "\n" + "...THE SENITMENT OF THIS TWEET IS ..:" + sentiment}
        requests.post(url= webhook_url, json = slackdata)
        time.sleep(3600)