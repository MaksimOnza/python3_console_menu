import requests


class OpenweathermapResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_data(self, city: str):
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?APPID={self.__access_key}&q={city}')
		data = response.json()
		return self.get_json(data)

	def get_json(self, data):
		json_data = {
			'temp': int((data['main']['temp'])-273),
			'desc': data['weather'][0]['description']
		}
		return json_data