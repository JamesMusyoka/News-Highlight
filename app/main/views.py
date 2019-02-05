#Imports
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_news,get_headlines
# from ..models import News,Headlines

#views

@main.route('/')
def index():
   """
   View root page function that returns the index page and its data
   """
   #   getting news
   general_news = get_news('general')
   technology_news = get_news('technology')
   health_news = get_news('health')
   business_news = get_news('business')
   sport_news = get_news('sport')
   entertainment_news = get_news('entertainment')
   science_news = get_news('science')

   title = 'Home - Top'


   search_news = request.args.get('search_query')

   if search_news:
       return redirect(url_for('search',news_name=search_news))
   else:
       return render_template('index.html', title = title, general = general_news, technology = technology_news,health = health_news,business = business_news,sport = sport_news,entertainment = entertainment_news,science = science_news )

@main.route('/search/<news_name>')
def search(news_name):
   '''
   View function to display the search results
   '''
   news_name_list = news_name.split(" ")
   news_name_format = "+".join(news_name_list)
   searched_news = search_news(news_name_format)
   title = f'search results for {news_name}'
   return render_template('search.html',news = searched_news)


@main.route('/headlines/<string:id>')
def headlines(id):
   """
   View headlinse from a specific source
   """
   headlines = get_headlines(id)
   title = f'{id}'

   return render_template('news.html',title = title,headlines = headlines)
