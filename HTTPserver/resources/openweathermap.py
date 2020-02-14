import requests


class OpenweathermapResource:

	def __init__(self, access_key: str):
		self.__access_key = access_key

	def get_temperature(self, city: str) -> int:
		response = requests.get(f'https://api.openweathermap.org/data/2.5/weather?APPID={self.__access_key}&q={city}')
		data = response.json()

		return (data['main']['temp']-273)