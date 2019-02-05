import os

class Config:
 """
 General configuration parent class
 """
 NEWS_API_BASE_URL = 'https://newsapi.org/v2/sources?language=en&category={}&apiKey={}'
 NEWS_API_SECONDARY_URL = 'https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
 NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
 HEADLINES_KEY = 'https://newsapi.org/v2/top-headlines?country=us&apiKey=597b0dec338d4c37a52b93e8570d3cf7'
 SOURCE_API = 'https://newsapi.org/v2/sources?apiKey=597b0dec338d4c37a52b93e8570d3cf7'
#  ARTICLE_API
 # SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
 """
 Production configuration child class
 Args:
   Config: The parent configuration class with General
   configuration settings
 """
 pass


class DevConfig(Config):
 """
 Development configuration child class
 Args:
   Config: The parent configuration class with General
   configuration settings
 """

 DEBUG = True


config_options = {
'development':DevConfig,
'production':ProdConfig
}
