class DisplayResponseData:

	def __init__(self, temperature):
		self.__temperature = temperature
		self.__display_temp(temperature)

	def __display_temp(self, temp):
		for iter in self.respons_param.output_param:
            temp = loaded_json[iter]
            loaded_json = temp
        if int(loaded_json) > 200:
            print("%.2f"%(loaded_json - 273))
        else:
            print(loaded_json)