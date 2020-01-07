from menu_items.menu_item import MenuItem 
from shows_images.simple_image import ShowImage

class DisplayItem(MenuItem):

	def start(self):
		ShowImage()

	def get_name(self):
		return "Display"

	def get_key_name(self):
		return "d"

	def get_key(self):
		return 'd'