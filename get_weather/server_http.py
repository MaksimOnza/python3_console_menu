import http.server
import socketserver
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.worldweatheronline import WorldweatheronlineResource
from resources.sinoptik import SinoptikResource
import config

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
		self.city = ''
		self.resource = ''
		self.send_response(200)
		self.send_header('content-type','text/html')
		self.end_headers()
		self.parsing(self.path)
		self.temperature = self.get_temperature(self.resource, self.city)
		self.wfile.write('Temperature in '.encode())
		self.wfile.write(self.city.encode())
		self.wfile.write(' => '.encode())
		self.wfile.write(str(self.temperature).encode())
		

	def parsing(self, string):
		first_symbol = string.find("?")
		start_param = string.find(RESOURCE, first_symbol)
		end_param = string.find("&", start_param)
		self.resource = string[start_param+len(RESOURCE)+1: end_param]
		start_param = string.find(CITY, end_param)
		self.city = string[start_param+len(CITY)+1: len(string)]

	def get_temperature(self, resource, city):
		temperature = resources[resource].get_temperature(city)
		return temperature

serv = http.server.HTTPServer(("localhost",PORT),HttpProcessor)
serv.serve_forever()


