import requests
from config import NEWS_API_KEY

def get_news():
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={NEWS_API_KEY}"
    
    response = requests.get(url)
    data = response.json()

    articles = data["articles"][:5]

    news_list = []
    for article in articles:
        news_list.append(article["title"])

    return news_list
