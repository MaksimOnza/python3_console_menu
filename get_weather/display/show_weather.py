from data.transit_data import TransitData
from connect.connect import Connect
from display.display_temp import DisplayTemp

class ShowWeather:

	def __init__(self):
		self.transit_data = TransitData
		self.web = self.get_web()
		self.city = self.get_city()
		self.type_web = self.get_type_web()
		self.web_connect = Connect(self.web, self.city, self.type_web)
		self.display = DisplayTemp(self.web)
		self.display.display_json_data(self.web_connect.to_display()) 


	def get_type_web(self):
		return self.transit_data.get_type_web()
	
	def get_web(self):
		return self.transit_data.print_web()

	def get_city(self):
		return self.transit_data.print_city()

	def show_weather(self):
		self.web_connect.display_weather()