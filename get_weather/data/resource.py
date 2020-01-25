from abc import ABC, abstractmethod

class Resource(ABC):

	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def get_key(self):
		pass

	@abstractmethod
	def get_list_name_param(self):
		pass

	@abstractmethod
	def get_output_param(self):
		pass