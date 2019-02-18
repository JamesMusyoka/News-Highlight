#Imports
from flask import render_template,request,redirect,url_for
from . import main
from ..request import get_quotes,get_random
from ..models import Quote,Random

#views

@main.route('/')
def index():
   """
   View root page function that returns the index page and its data
   """

   title = 'The Random Quotes'


   search_quotes = request.args.get('search_query')

   if search_quotes:
       return redirect(url_for('search',quotes_name=search_quotes))
   else:
       return render_template('index.html', title = title)

@main.route('/search/<quotes_name>')
def search(quotes_name):
   '''
   View function to display the search results
   '''
   quotes_name_list = quotes_name.split(" ")
   quotes_name_format = "+".join(quotes_name_list)
   searched_quotes = search_quotes(quotes_name_format)
   title = f'search results for {quotes_name}'
   return render_template('search.html',quotes = searched_quotes)


@main.route('/quotes/<id>')
def quotes(id):
   """
   View random from a specific source
   """
   random = get_random(id)
   print (source)

   title = f'{id}'

   return render_template('source.html',title = title, myrandom = random, myrandomid = id)
