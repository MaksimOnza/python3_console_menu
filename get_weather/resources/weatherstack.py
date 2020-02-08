import requests


class WeatherstackResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_temperature(self, city: str) -> int:
		response = requests.get(f'https://api.weatherstack.com/current?access_key={self.__access_key}&query={city}')
		data = response.json()
		
		return data['current']['temperature']