from resources.worldweatheronline import WorldweatheronlineResource
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.sinoptik import SinoptikResource
from urllib.parse import parse_qs, urlparse
from cashe2 import CacheData
import http.server
import config
import json
import time


PORT = 8000
CITY = 'city'
RESOURCE = 'resource'
resources = {
	'weatherstack': WeatherstackResource(config.WEATHERSTACK_ACCESS_KEY),
	'openweathermap': OpenweathermapResource(config.OPENWEATHERMAP_ACCESS_KEY),
	'worldweatheronline': WorldweatheronlineResource(config.WORLDWEATHERONLINE_ACCESS_KEY),
	'sinoptik': SinoptikResource()
}
#form = cgi.FieldStorage()


class HttpProcessor(http.server.BaseHTTPRequestHandler):
			
	
	operator = CacheData()

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		query_components = self.parsing()
		city = ' '.join(query_components[CITY])
		resource = ' '.join(query_components[RESOURCE])
		data_weather = self.operator.get(resource+city)
		if data_weather is None:
			data_weather = self.get_data_weather(resource, city)	
			self.operator.set(resource+city, data_weather)
		self.wfile.write((city).encode())
		self.wfile.write(json.dumps(data_weather).encode())


	def get_data_weather(self, resource, city):
		data_weather = resources[resource].get_data(city)
		return data_weather

	
	def parsing(self):
		query_components = parse_qs(urlparse(self.path).query)
		return query_components



serv = http.server.HTTPServer(("localhost", PORT), HttpProcessor)
serv.serve_forever()
