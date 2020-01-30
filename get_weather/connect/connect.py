import http.client
from lxml import html
import requests
import json
from data.data_link import DataLink
from data.transit_data import TransitData
from data.sinoptyk_data import SinoptykData

class Connect:

	list_type_web = ['api', 'html']

	def __init__(self, web, city, type_web):
		self.__city = city
		if type_web == self.list_type_web[0]:
			self.__web = web
			self.get_api_params()
			self.connecting()
		elif type_web == self.list_type_web[1]:

			sin = SinoptykData()
			self.www = web
			self.city = city
			self.element = sin.get_element()
			self.name_properties = sin.get_name_properties()
			self.properties = sin.get_properties()
			self.to_display_html()

	def get_api_params(self):
		self.__query_city_name = TransitData.get_name_query_city()
		self.__query_key_name = TransitData.get_name_query_key()
		self.__key = TransitData.get_key()
		self.__after_web = TransitData.get_add_link()

	def connecting(self):
		self.conn = http.client.HTTPConnection(f'api.{self.__web}')
		self.conn.request("GET", f'/{self.__after_web}?{self.__query_key_name}={self.__key}&{self.__query_city_name}={self.__city}')
		self.response = self.conn.getresponse()

	#Переделать вывод, сделать универсальным
	def to_display(self):
		body = self.response.read()
		loaded_json = json.loads(body)
		return loaded_json

	def to_display_html(self):
		print(f"{self.www} {self.city} {self.element} {self.properties} {self.name_properties}")
		
		page = requests.get(f'https://{self.www}/погода-{self.city}')
		tree = html.fromstring(page.content)
		some = tree.xpath(f'//{self.element}[@{self.properties}={self.name_properties}]/text()')
		print(some[0])
