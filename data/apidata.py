import requests
from dotenv import load_dotenv
import os



load_dotenv()
Tennis_API_KEY=os.getenv('Tennis_API_KEY')
news_API_KEY=os.getenv('NEWS_API_KEY')

### API TENNIS https://api-tennis.com/documentation
response_tennis=requests.get(f'https://api.api-tennis.com/tennis/?method=get_events&APIkey={Tennis_API_KEY}')

### https://www.thenewsapi.com/documentation
response_news=requests.get(f'https://api.thenewsapi.com/v1/news/top?api_token={news_API_KEY}')


print(response_tennis.json())
print(response_news.json())