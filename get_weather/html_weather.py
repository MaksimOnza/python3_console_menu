from lxml import html
import requests

www = 'google.com'
page = requests.get(f'https://sinoptik.ua/погода-харьков')
tree = html.fromstring(page.content)
some = tree.xpath('//p[@class="today-temp"]/text()')
print(some[0])
