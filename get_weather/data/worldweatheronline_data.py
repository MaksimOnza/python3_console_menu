from data.web_resource import WebResource


class WorldweatheronlineData(WebResource):

	def __init__(self):
		self.name = 'worldweatheronline.com'
		self.key = 'd48ab845d78e492081b192620202001'
		self.add_link = 'premium/v1/weather.ashx'
		self.output_param = ['data', 'current_condition',0 ,'temp_C']
		self.list_name_param = {'key': 'format=json&key', 'city': 'q'}

	def get_name(self):
		return self.name

	def get_key(self):
		return self.key

	def get_list_name_param(self):
		return self.list_name_param

	def get_output_param(self):
		return self.output_param

	def get_add_link(self):
		return self.add_link