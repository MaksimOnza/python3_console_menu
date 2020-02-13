import http.server
import socketserver
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.worldweatheronline import WorldweatheronlineResource
from resources.sinoptik import SinoptikResource
import config
import urllib.parse as urllib

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
		
		self.url_parsing(self.path)

		self.temperature = self.get_temperature(self.resource, self.city)
		self.wfile.write('Temperature in '.encode())
		self.wfile.write((self.listToString(self.city)).capitalize().encode())
		self.wfile.write(' => '.encode())
		self.wfile.write(str(self.temperature).encode())
		self.wfile.write('*C'.encode())
		
	
	def get_temperature(self, resource, city):
		temperature = resources[self.listToString(resource)].get_temperature(self.listToString(city))
		return temperature


	def url_parsing(self, url):
		base_url = urllib.urlparse(url)
		split_after_url = base_url.query.split(' ')[0]
		dict_param = urllib.parse_qs(split_after_url)
		self.resource = dict_param[RESOURCE]
		self.city = dict_param[CITY]
		return dict_param


	def listToString(self, s):
		str1 = ""  
		return (str1.join(s)) 
	


serv = http.server.HTTPServer(("localhost",PORT),HttpProcessor)
serv.serve_forever()
