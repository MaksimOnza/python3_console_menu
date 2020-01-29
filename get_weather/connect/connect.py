import http.client
import json
from data.data_link import DataLink
from data.transit_data import TransitData

class Connect:


	def __init__(self, web, city):
		self.__web = web
		self.__city = city
		self.__query_city_name = TransitData.get_name_query_city()
		self.__query_key_name = TransitData.get_name_query_key()
		self.__key = TransitData.get_key()
		self.__after_web = TransitData.get_add_link()
		self.connecting()


	def connecting(self):
		self.conn = http.client.HTTPConnection(f'api.{self.__web}')
		self.conn.request("GET", f'/{self.__after_web}?{self.__query_key_name}={self.__key}&{self.__query_city_name}={self.__city}')
		self.response = self.conn.getresponse()
		# вместо output -> response

	def to_display(self):
		body = self.response.read()
		loaded_json = json.loads(body)
		return loaded_json
