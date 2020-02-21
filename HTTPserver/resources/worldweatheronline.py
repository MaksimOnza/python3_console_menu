import requests
import time


class WorldweatheronlineResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_data(self, city: str):
		response = requests.get(f'https://api.worldweatheronline.com/premium/v1/weather.ashx?format=json&key={self.__access_key}&q={city}')
		data = response.json()
		return self.get_json(data)

	def get_json(self, data):
		json_data = {
			'temp': data['data']['current_condition'][0]['temp_C'],
			'desc': data['data']['current_condition'][0]['weatherDesc'][0]['value']
		}
		return json_data
