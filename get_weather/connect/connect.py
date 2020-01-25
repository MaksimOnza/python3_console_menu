import http.client
import json
from data.data_link import DataLink
from top_list import TopList

class Connect:


	def __init__(self, web, city):
		#self.web_obj = DataLink()
		#if web in self.web_obj.dic_web_key:
		self.__web = web
		self.__city = city
		self.__query_city_name = TopList.get_name_query_city()
		self.__query_key_name = TopList.get_name_query_key()
		self.__key = TopList.get_key()
		self.__after_web = TopList.get_add_link()
		self.connecting()


	def connecting(self):
		self.conn = http.client.HTTPConnection(f'api.{self.__web}')
		self.conn.request("GET", f'/{self.__after_web}?{self.__query_key_name}={self.__key}&{self.__query_city_name}={self.__city}')
		self.output = self.conn.getresponse()
		# вместо output -> response

	def to_display(self):
		body = self.output.read()
		loaded_json = json.loads(body)
		return loaded_json
