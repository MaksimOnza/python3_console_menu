from resources.worldweatheronline import WorldweatheronlineResource
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.sinoptik import SinoptikResource
from urllib.parse import parse_qs, urlparse
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

Handler = http.server.BaseHTTPRequestHandler


class HttpProcessor(http.server.BaseHTTPRequestHandler):
		
	kesh_dict = {}

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		query_components = self.parsing()
		city = query_components[CITY][0]
		resource = query_components[RESOURCE][0]
		current_time = time.time()
		if (city+resource in self.kesh_dict.keys()):
			if ((current_time - self.kesh_dict['time']) > 3600):
				data_weather = self.get_data_weather(resource, city)
				temperature = data_weather['temp']
				description = data_weather['desc']
			else:
				temperature =  self.kesh_dict[city]['temp']
				description = self.kesh_dict[city]['desc']
		else:
			data_weather = self.get_data_weather(resource, city)
			temperature = data_weather['temp']
			description = data_weather['desc']
		self.kesh_dict = {
			city+resource: {	
					'temp': temperature,
					'desc': description,
					},
			'time': time.time()
			}
		self.wfile.write(json.dumps({
			'name_city': city,
			'temperature': temperature,
			'description': description
			}).encode())


	def get_data_weather(self, resource, city):
		data_weather = resources[resource].get_data(city)
		return data_weather

	
	def parsing(self):
		query_components = parse_qs(urlparse(self.path).query)
		return query_components


serv = http.server.HTTPServer(("localhost",PORT),HttpProcessor)
serv.serve_forever()


#идеальный код книга
#рефакторинг кода в серве(ифэлс зло)
#аналог на ПХП без внешних библ PHP.net
#
#
#
#
#
#
#