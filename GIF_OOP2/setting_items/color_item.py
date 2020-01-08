from menu_items.menu_item import MenuItem
from menu import Menu 

class ColorItem(MenuItem):

	def __init__(self, items):
		self.__color_menu = Menu(items)

	def start(self):
		self.__color_menu.start()


	def get_name(self):
		return "Color"


	def get_key_name(self):
		return 'c'


	def get_key(self):
		return 'c'