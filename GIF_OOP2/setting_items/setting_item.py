from menu_items.menu_item import MenuItem 
from menu import Menu 

class SettingItem(MenuItem):
	def __init__(self, items):
		self.__setting_menu = Menu(items)

	def start(self):
		self.__setting_menu.start()

	def get_name(self):
		return "Setting"

	def get_key_name(self):
		return "s"

	def get_key(self):
		return 's'