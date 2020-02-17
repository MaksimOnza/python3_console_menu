from resources.worldweatheronline import WorldweatheronlineResource
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.sinoptik import SinoptikResource
from urllib.parse import parse_qs, urlparse
import http.server
import config
import json



PORT = 8000
CITY = 'city'
RESOURCE = 'resource'
resources = {
	'weatherstack': WeatherstackResource(config.WEATHERSTACK_ACCESS_KEY),
	'openweathermap': OpenweathermapResource(config.OPENWEATHERMAP_ACCESS_KEY),
	'worldweatheronline': WorldweatheronlineResource(config.WORLDWEATHERONLINE_ACCESS_KEY),
	'sinoptik': SinoptikResource()
}
weather_data_dict = {
	'weatherstack': ['temperature', 'weather_descriptions'],
	'openweathermap': [['main', 'temp'], ['weather', 0,  'description']],
	'worldweatheronline': [['current_condition', 0, 'temp_C'], ['current_condition', 0, 'weatherDesc', 0, 'value']]
}

Handler = http.server.BaseHTTPRequestHandler


class HttpProcessor(http.server.BaseHTTPRequestHandler):
		

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.query_components = self.parsing()
		self.city = self.query_components[CITY][0]
		self.resource = self.query_components[RESOURCE][0]
		self.data_weather = self.get_data_weather(self.resource, self.city)
		self.temperature = self.get_temp_descript(self.data_weather, self.resource, 0)
		self.description = self.get_temp_descript(self.data_weather, self.resource, 1)
		self.wfile.write(json.dumps({
			'name_city': self.city,
			'temperature': self.temperature,
			'description': self.description
			}).encode())
		
	
	def get_data_weather(self, resource, city):
		data_weather = resources[resource].get_temperature(city)
		return data_weather

	def get_temp_descript(self, data, resource, index):
		query_list = weather_data_dict[resource][index]
		output = query_list
		if isinstance(query_list, list):
			for line in list(query_list):
				temp = data[line]
				data = temp
				output = data
		else:
			output = data[query_list]
		return output
	

	def parsing(self):
		query_components = parse_qs(urlparse(self.path).query)
		return query_components


serv = http.server.HTTPServer(("localhost",PORT),HttpProcessor)
serv.serve_forever()
