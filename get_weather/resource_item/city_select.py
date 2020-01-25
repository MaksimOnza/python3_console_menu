from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList
from data.key_symbol import KeySymbol

class CitySelect(MenuItem):

	def __init__(self):
		self.__key = KeySymbol()

	def start(self):
		print("Enter the City or town")
		enter_city = input()
		TopList.selected_city = enter_city

	def get_name(self):
		return "CitySelect"

	def get_key_name(self):
		return self.__key.KEY_SELECT_CITY

	def get_key(self):
		return self.__key.KEY_SELECT_CITY