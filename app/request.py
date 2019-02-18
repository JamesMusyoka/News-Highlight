import urllib.request,json
from .models import Quotes, Random

#Getting api key
api_key = None

#Getting newsapi base url
base_url = None

#Getting newsapi secondary url
secondary_url = None

# # Getting news url
# news_url = None

# # Getting headlines url
# headlines_url = None

def configure_request(app):
   global api_key,base_url,secondary_url
   api_key =  app.config['QUOTES_API_KEY']
   base_url =  app.config['BASE_URL']
   secondary_url = app.config['QUOTES_API_SECONDARY_URL']


def get_quotes(category):
 """
 Function that gets the json response to our url request
 """
 get_quotes_url = base_url.format(category,api_key)

 with urllib.request.urlopen(get_quotes_url) as url:
   get_quotes_data = url.read()
   get_quotes_response= json.loads(get_quotes_data)

   quotes_results = None

   if get_quotes_response['sources']:
     quotes_results_list = get_quotes_response['sources']
     news_results = process_results(quotes_results_list)

 return quotes_results


def process_results(quotes_results_list):
 
 quotes_results = []
 for quotes_item in news_results_list:
   id = quotes_item.get('id')
   name = quotes_item.get('name')
   url = quotes_item.get('url')
   category = quotes_item.get('category')
   description = quotes_item.get('description')
   country = quotes_item.get('country')


   if name:
     quotes_object = Quotes(id,name,url,category,description
     )
     quotes_results.append(quotes_object)

 return Quotes_results


def search_quotes(news_name):

    search_quotes_url = 'http://quotes.stormconsultancy.co.uk/{}.json'.format(api_key, news_name)
    with urllib.request.urlopen(search_quotes_url) as url:
        search_quotes_data = url.read()
        search_quotes_response = json.loads(search_quotes_data)

        search_quotes_results = None

        if search_quotes_response['sources']:
            search_quotes_list = search_quotes_response['sources']
            search_quotes_results = process_results (search_quotes_list)

    return search_quotes_results


def get_random(id):
 """
 Function that gets the json response to our url request
 """
 get_random_url = secondary_url.format(id,api_key)

 with urllib.request.urlopen(get_random_url) as url:
   get_random_data = url.read()
   get_random_response= json.loads(get_random_data)

   random_results = None

   if get_random_response['random']:
     random_results_list = get_random_response['random']
     random_results = process_random(random_results_list)

 return random_results


def process_random(random_results_list):
 
 random_results = []
 for random_item in random_list:
     
   id = random_item.get('id')
   title = random_item.get('title')
   description = random_item.get('description')
   url =  random_item.get('url')
   urlToImage = random_item.get('urlToImage')
   publishedAt = random_item.get('publishedAt')

   if title:
     random_object = random(id,title,description,url,urlToImage,publishedAt)
     random_results.append(random_object)

 return random_results