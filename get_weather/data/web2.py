from data.resource import Resource


class Web2(Resource):

	def __init__(self):
		self.name = 'openweathermap.org'
		self.key = '55fc030a936d5e205ca578d8a03011ba'
		self.add_link = 'data/2.5/weather'
		self.output_param = ['main', 'temp']
		self.list_name_param = {'key': 'APPID', 'city': 'q'}

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