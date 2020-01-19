import http.client
import json

class Connect:

	dic_web_key = {
			"weatherstack.com":'719d3fe6203f73509524e0bca348cb53',
			"":'',
			"":''
			}

	def __init__(self, web, city):
		self.mode = "current"
		self.key = self.get_key(web)
		self.conn = http.client.HTTPConnection(f"api.{web}")
		self.conn.request("GET", f'/{self.mode}?access_key={self.key}&query={city}')
		

	def get_key(self, web):
		return self.dic_web_key[web]	

	def display_weather(self):
		output = self.conn.getresponse()
		body = output.read()
		loaded_json = json.loads(body)
		print(loaded_json['current']['temperature'])
