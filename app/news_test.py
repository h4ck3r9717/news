import unittest
from models import news
News = news.News

class NewsTest(unittest.TestCase):
    '''
    Test class for testing the behaviour of the news class
    '''
    def setUp(self):
        '''
        setup method to run before the test
        '''
        self.new_news = News('reloaded.com', 'kinyae', 'Life in Technologies', 'How to stay updated in tech world', 'https://www.bbc.co.uk/news/technology-58124495', 'https://ichef.bbci.co.uk/news/1024/branded_news/33F6/production/_119820331_c04c0588-a2c0-4530-93d6-7380afb5b022.jpg',  '2021-08-07T01:09:09Z')
        
    def test_instance(self):
        self.assertTrue(isinstance(self.new_news, News))
 
if __name__ == "__main__":
    unittest.main()        
            