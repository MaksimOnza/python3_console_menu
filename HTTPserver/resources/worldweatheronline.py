import requests

class WorldweatheronlineResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_temperature(self, city: str) -> int:
		response = requests.get(f'https://api.worldweatheronline.com/premium/v1/weather.ashx?format=json&key={self.__access_key}&q={city}')

		data = response.json()

		return int(data['data']['current_condition'][0]['temp_C'])