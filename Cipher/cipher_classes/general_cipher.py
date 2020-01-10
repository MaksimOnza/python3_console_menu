from abc import ABC, abstractmethod

class GeneralCipher(ABC):

	@abstractmethod
	def coder(self):
		pass

	@abstractmethod
	def decoder(self):
		pass