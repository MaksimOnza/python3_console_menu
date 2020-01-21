import http.client
import json
from data.data_link import DataLink

class Connect:

	dic_web_key = [
			"weatherstack.com",
			"openweathermap.org",
			"worldweatheronline.com"
			]

	def __init__(self, web, city):
		self.web_obj = DataLink()
		if web in self.dic_web_key:
			self.__web = web
			self.__city = city
			self.__query_city_name = self.web_obj.query_link['query_city_name'][web]
			self.__query_key_name = self.web_obj.query_link['query_key_name'][web]
			self.__key = self.web_obj.query_link['key'][web]
			self.__after_web = self.web_obj.query_link['after_web'][web]
			self.element_first_level = self.web_obj.query_link['first_level'][self.__web]
			self.elemene_second_level = self.web_obj.query_link['temperature'][self.__web]
			self.connecting()
		else:
			print("Wrong web adres")


	def connecting(self):
		self.conn = http.client.HTTPConnection(f'api.{self.__web}')
		self.conn.request("GET", f'/{self.__after_web}?{self.__query_key_name}={self.__key}&{self.__query_city_name}={self.__city}')

	def get_key(self, web):
		return self.dic_web_key[web]	

	def display_weather(self):
		output = self.conn.getresponse()
		body = output.read()
		loaded_json = json.loads(body)
		print(loaded_json[self.element_first_level][self.elemene_second_level])#