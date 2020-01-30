from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from connect.connect import Connect
from display.display_temp import DisplayTemp
from data.type_web import TypeWeb

class ShowWeather:

	def __init__(self):
		self.type_web = self.get_type_web()
		if self.type_web == 'api':
			self.transit_data = TransitData
			self.city = self.get_city()
			self.web = self.get_web()
			self.web_connect = Connect(self.web, self.city, self.type_web)
			self.display = DisplayTemp(self.web)
			self.display.display_json_data(self.web_connect.to_display())
		elif self.type_web == 'html':
			self.transit_data = HTMLTransitData
			self.city = self.get_city()
			self.web = self.get_www()
			self.web_connect = Connect(self.web, self.city, self.type_web)


	def get_type_web(self):
		return TypeWeb.get_type_web()
	
	def get_web(self):
		return self.transit_data.print_web()

	def get_www(self):
		return HTMLTransitData.print_web()

	def get_city(self):
		return self.transit_data.print_city()

	def show_weather(self):
		self.web_connect.display_weather()