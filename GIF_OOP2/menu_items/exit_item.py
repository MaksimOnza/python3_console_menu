from menu_items.menu_item import MenuItem

class ExitItem(MenuItem):
	
	def start(self):
		print("Exit")

	def get_name(self):
		return "Exit"

	def get_key_name(self):
		return "e"

	def get_key(self):
		return 'e'
