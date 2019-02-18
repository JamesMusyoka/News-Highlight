import requests

def getquotes():
  url = 'http://quotes.stormconsultancy.co.uk/random.json'
  call = requests.get(url)
  quote = call.json()
  return quote



