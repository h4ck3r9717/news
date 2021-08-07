from app import app
import urllib.request, json
from .models import news

News = news.News

#Get the api key
api_key = app.config['NEWS_API_KEY']

#Get news api url
base_url = app.config['NEWS_API_BASE_URL']