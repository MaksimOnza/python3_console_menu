import http.client
import json
from data.data_link import DataLink

class Connect:


	def __init__(self, web, city):
		self.web_obj = DataLink()
		if web in self.web_obj.dic_web_key:
			self.__web = web
			self.__city = city
			self.__query_city_name = self.web_obj.query_link['query_city_name'][web]
			self.__query_key_name = self.web_obj.query_link['query_key_name'][web]
			self.__key = self.web_obj.query_link['key'][web]
			self.__after_web = self.web_obj.query_link['after_web'][web]
			self.connecting()
		else:
			print("Wrong web adres")


	def connecting(self):
		self.conn = http.client.HTTPConnection(f'api.{self.__web}')
		self.conn.request("GET", f'/{self.__after_web}?{self.__query_key_name}={self.__key}&{self.__query_city_name}={self.__city}')
		self.output = self.conn.getresponse()

	def to_display(self):
		body = self.output.read()
		loaded_json = json.loads(body)
		return loaded_json
