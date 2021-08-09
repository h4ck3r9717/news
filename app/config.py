from instance.config import NEWS_API_KEY


class Config:
    '''
    Configuration parent class
    '''
    NEWS_API_BASE_URL =  'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
    ARTICLES_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'


class ProdConfig(Config):
    '''
    production configuration class
    '''
    pass

class DevConfig(Config):
    '''
    Development configuration class
    '''
    DEBUG = True
    