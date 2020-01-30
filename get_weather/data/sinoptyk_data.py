class SinoptykData:

	def __init__(self):
		self.type_web = 'html'
		self.__www = 'sinoptik.ua'
		self.__element = 'p'
		self.__properties = 'class'
		self.__name_properties = '"today-temp"'

	def get_type_web(self):
		return self.type_web

	def get_www(self):
		return self.__www

	def get_element(self):
		return self.__element

	def get_properties(self):
		return self.__properties

	def get_name_properties(self):
		return self.__name_properties