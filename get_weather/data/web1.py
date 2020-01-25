from data.resource import Resource


class Web1(Resource):

	def __init__(self):
		self.name = 'weatherstack.com'
		self.key = '719d3fe6203f73509524e0bca348cb53'
		self.add_link = 'current'
		self.output_param = ['current', 'temperature']
		self.list_name_param = {'key': 'access_key', 'city': 'query'}
	
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