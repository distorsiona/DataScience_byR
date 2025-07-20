
import tweepy
import pandas as pd
from typing import List
import os

class TwitterClient:
    def __init__(self, bearer_token: str):
        self.client = tweepy.Client(bearer_token=bearer_token)

    def buscar_tweets(self, query: str, max_tweets: int = 100) -> pd.DataFrame:
        tweets_data = []

        response = self.client.search_recent_tweets(
            query=query,
            tweet_fields=["created_at", "lang", "text"],
            max_results=100
        )

        for tweet in response.data[:max_tweets]:
            tweets_data.append({
                "texto": tweet.text,
                "fecha": tweet.created_at,
                "idioma": tweet.lang
            })

        df = pd.DataFrame(tweets_data)
        return df
