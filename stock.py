import urllib.request

symbol = 'aapl'
form = 'abp'

url = 'http://finance.yahoo.com/d/quotes.csv?s={}&f={}'.format(symbol, form)

response = urllib.request.urlopen(url)
html = response.read()

print(response)




