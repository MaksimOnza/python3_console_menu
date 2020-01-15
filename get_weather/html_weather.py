from lxml import html
import requests

www = 'google.com'
page = requests.get(f'https://sinoptik.ua/погода-харьков')
tree = html.fromstring(page.content)
some = tree.xpath('//p[@class="today-temp"]/text()')
print(some[0])

page = requests.get('http://econpy.pythonanywhere.com/ex/001.html')
tree = html.fromstring(page.content)

#This will create a list of buyers:
buyers = tree.xpath('//div[@title="buyer-name"]/text()')
#This will create a list of prices
prices = tree.xpath('//span[@class="item-price"]/text()')
print(buyers)
print(prices)
