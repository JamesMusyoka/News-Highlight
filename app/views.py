# from flask import render_template, request, redirect, url_for
# from app import app
# from .request import get_news, search_news,get_headlines
# # from .request import get_article, search_article


# # Views
# @app.route('/')
# def index():

#     '''
#     View root page function that returns the index page and its data
#     '''
#      #get sources
#     general = get_news('general')
#     technology = get_news('technology')
#     business = get_news('business')
#     entertainment = get_news('entertainment')
#     sports = get_news('sports')

#     title = 'Home - Welcome to the most informative news site online!!!'

#     # search_source = request.args.get('search_query')

#     return render_template('index.html', title = title, general = general, technology = technology, business = business, entertainment = entertainment, sports = sports)



# @app.route('/search/<news_name>')
# def search(news_name):
#     '''
#     View function to display search results
#     '''
#     news_name_list = news_name.split(" ")
#     news_name_format = "+".join(news_name_list)
#     searched_news = search_news(news_name_format)
#     title = f'search results for {news_name}'

#     return render_template('search.html', news = searched_news)

#     #get articles
#     # article_general = get_article('general')
#     # print(article_general)

#     title = 'Home - Welcome to the most informative news site online!!!'
#     return render_template('index.html', title = title, general = news_general)

   

# @app.route('/news/<string:id>')
# def source(id):

#     '''
#     View news page function that returns the news details page and its data
#     '''
#     news = get_article(id)
#     print(source)
    
#     return render_template('source.html',source = source)