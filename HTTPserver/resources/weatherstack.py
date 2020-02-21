import requests
import json


class WeatherstackResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_data(self, city: str):
		response = requests.get(f'http://api.weatherstack.com/current?access_key={self.__access_key}&query={city}')
		data = response.json()
		return self.get_json(data)

	def get_json(self, data):
		json_data = {
			'temp': data['current']['temperature'],
			'desc': data['current']['weather_descriptions'][0]
		}
		return json_data