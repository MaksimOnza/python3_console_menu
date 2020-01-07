import platform, os

class Menu:
	def __init__(self, items):
		self.__items = items

	def start(self):
		if(platform.system() == 'Linux'):
			os.system('clear')
		if(platform.system() == 'Windows'):
			os.system('cls')

		for item in self.__items:
			print(item.get_name() + " -> " + item.get_key_name())

		key = input()
		for item in self.__items:
			if item.get_key() == key:
				item.start()
