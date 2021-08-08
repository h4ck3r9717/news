from app import app
import urllib.request, json
from .models import news

News = news.News

#Get the api key
api_key = app.config['NEWS_API_KEY']

#Get news api url
base_url = app.config['NEWS_API_BASE_URL']

def get_news(category):
    '''
    Function that gets the response to our request
    '''
    get_news_url = base_url.format(category, api_key)
    
    with urllib.request.urlopen(get_news_url) as url:
        get_news_data = url.read()
        get_news_response = json.loads(get_news_data)
        
        news_results = None
        
        if get_news_response['sources']:
            news_results_list = get_news_response['sources']
            news_results = process_results(news_results_list)
            
    return  news_results 

def process_results(news_list):
    '''
    Function that processes the results and transforms them to a list of objects 
    '''       
    news_results = []
    for news_item in news_list:
        name = news_item.get('name')
        description = news_item.get('description')
        url = news_item.get('url')
        country = news_item.get('country')
        
        if url:
            news_object = News( name, description, url, country)
            news_results.append(news_object)
        
    return news_results    

