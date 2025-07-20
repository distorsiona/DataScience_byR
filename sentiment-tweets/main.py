from dotenv import load_dotenv
from src.twitter_client import TwitterClient
import os

load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")

#instancia al cliente
client = TwitterClient(BEARER_TOKEN)

# Buscar tweets con una palabra clave
df_tweets = client.buscar_tweets("terremoto", max_tweets=30)
print(df_tweets.head())
