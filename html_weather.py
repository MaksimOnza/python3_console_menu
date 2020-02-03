from lxml import html
import requests

www = 'sinoptik.ua'
element = 'p'
properties = 'class'
name_properties = '"today-temp"'

city = input()
page = requests.get(f'https://{www}/погода-{city}')
tree = html.fromstring(page.content)
some = tree.xpath(f'//{element}[@{properties}={name_properties}]/text()')
print(some[0])
