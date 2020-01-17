from abc import ABC, abstractmethod

class MenuItem(ABC):

	@abstractmethod
	def start(self):
		pass

	@abstractmethod
	def get_name(self):
		pass

	@abstractmethod
	def get_key_name(self):
		pass

	@abstractmethod
	def get_key(self):
		pass