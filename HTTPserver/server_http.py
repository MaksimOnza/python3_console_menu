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

Handler = http.server.BaseHTTPRequestHandler


class HttpProcessor(http.server.BaseHTTPRequestHandler):
		

	def do_GET(self):
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.query_components = self.parsing()
		self.city = self.query_components[CITY][0]
		self.resource = self.query_components[RESOURCE][0]
		self.weather = self.get_weather(self.resource, self.city)
		self.temperature = self.weather['temperature']
		self.description = self.weather['weather_descriptions']
		self.wfile.write(json.dumps({
			'name_city': self.city,
			'temperature': self.temperature,
			'description': self.description
			}).encode())
		
	
	def get_weather(self, resource, city):
		weather = resources[resource].get_temperature(city)
		return weather


	def parsing(self):
		query_components = parse_qs(urlparse(self.path).query)
		return query_components


serv = http.server.HTTPServer(("localhost",PORT),HttpProcessor)
serv.serve_forever()
