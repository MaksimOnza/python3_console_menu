import requests
from lxml import html


class SinoptikResource:

	def get_temperature(self, city: str) -> int:
		page = requests.get(f'https://sinoptik.ua/погода-{city}')
		tree = html.fromstring(page.content)
		temperature_str = tree.xpath(f'//p[@class="today-temp"]/text()')[0]
		
		return int(temperature_str[:-2])