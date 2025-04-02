import requests
from dotenv import load_dotenv
import os
import time
import datetime
import pandas as pd
from sqlalchemy import create_engine


load_dotenv()
Tennis_API_KEY=os.getenv('Tennis_API_KEY')
news_API_KEY=os.getenv('NEWS_API_KEY')

postgres_user=os.getenv('POSTGRES_USER')
postgres_password=os.getenv('POSTGRES_PASSWORD')

### API TENNIS https://api-tennis.com/documentation
response_tennis=requests.get(f'https://api.api-tennis.com/tennis/?method=get_events&APIkey={Tennis_API_KEY}')

### https://www.thenewsapi.com/documentation
response_news=requests.get(f'https://api.thenewsapi.com/v1/news/top?api_token={news_API_KEY}')


# print(response_tennis.json())
# print(response_news.json())

connection_url=f'postgresql+psycopg2://{postgres_user}:{postgres_password}@localhost:5432/tennis_db'
engine=create_engine(connection_url)



def get_ranking(tennis_api_key:str, engine,dtype_mapping:dict):
    response_atp_standing=requests.get(f'https://api.api-tennis.com/tennis/?method=get_standings&event_type=atp&APIkey={tennis_api_key}')
    atp_standings=response_atp_standing.json()
    df_ranking=pd.DataFrame(atp_standings['result'])
    df_ranking['timestamp']=time.time()
    df_ranking=df_ranking.rename(columns={'place':'ranking'})
    df_ranking.to_sql('player_ranking',con=engine, if_exists='replace', index=False,dtype=dtype_mapping)

    return 'success'

from sqlalchemy import Integer, String, Float

dtype_mapping={
    'ranking': Integer,
    'player': String(255) ,
    'player_key': Integer,
    'league': String(255),
    'movement':String(255),
    'country':String(255),
    'points':Float,
    'timestamp': Float,
}

df_ranking=get_ranking(tennis_api_key=Tennis_API_KEY, engine=engine,dtype_mapping=dtype_mapping)

df_ranking.__class__