class DisplayResource:

	__dict_func = {	"first_item": "data/display_data/file1.txt",
					"second_item": "name_file2",
					"third_item": "name_file3"}

	def __init__(self, strin):
		self.__param = strin
		self.name_file = self.get_name_file()


	def start(self):
		display_text = open(self.name_file)
		print(display_text.read())
		display_text.close()
		input()	

	def get_name_file(self):
		#return "first_item1.txt"
		return self.__dict_func["first_item"]