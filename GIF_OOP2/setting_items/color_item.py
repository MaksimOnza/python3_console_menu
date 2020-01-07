from menu_items.menu_item import MenuItem

class ColorItem(MenuItem):

	def start(self):
		print("Color")


	def get_name(self):
		return "Color"


	def get_key_name(self):
		return 'c'


	def get_key(self):
		return 'c'