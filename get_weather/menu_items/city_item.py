from menu_items.menu_item import MenuItem
from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.key_symbol import KeySymbol
from data.type_web import TypeWeb

class CityItem(MenuItem):

	def __init__(self):
		self.__key = KeySymbol()

	def start(self):
		print("Enter the City or town")
		enter_city = input()
		if TypeWeb.get_type_web() == 'api':
			TransitData.selected_city = enter_city
		elif TypeWeb.get_type_web() == 'html':
			HTMLTransitData.selected_city = enter_city

	def get_name(self):
		return "CitySelect"

	def get_key_name(self):
		return self.__key.KEY_SELECT_CITY

	def get_key(self):
		return self.__key.KEY_SELECT_CITY