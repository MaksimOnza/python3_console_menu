from top_list import TopList
from connect.connect import Connect

class ShowWeather:

	def __init__(self):
		self.top_list = TopList()
		self.web = self.get_web()
		self.city = self.get_city()
		self.show = Connect(self.web, self.city)
	
	def get_web(self):
		return self.top_list.print_web()

	def get_city(self):
		return self.top_list.print_city()

	def show_weather(self):
		self.show.display_weather()