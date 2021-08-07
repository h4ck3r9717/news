class Config:
    '''
    Configuration parent class
    '''
    pass

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
    