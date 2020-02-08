from menu_items.menu_item import MenuItem
from data.key_symbol import KeySymbol

class CityItem(MenuItem):

	def __init__(self, state):
		self.__key = KeySymbol()
		self.__state= state

	def start(self):
		print("Enter the City or town")
		print('\033[91m'+'If selected WEB = Sinoptyk')
		print('Enter a city on russia'+'\033[0m')
		self.__state.city = input()

	def get_name(self):
		return "CitySelect"

	def get_key_name(self):
		return self.__key.KEY_SELECT_CITY

	def get_key(self):
		return self.__key.KEY_SELECT_CITY