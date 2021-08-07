from flask import render_template
from app import app
from .request import get_news

#views 
@app.route('/')
def index():
    '''
    function that returns the index page and its data 
    '''
    #Get popular news
    popular_news = get_news('popular')
    print(popular_news)
    title = 'Welcome to Your News Agent'
    return render_template('index.html', title = title, popular = popular_news)