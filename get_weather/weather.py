import http.client
import requests

key = '719d3fe6203f73509524e0bca348cb53'
city = "London"
mode = 'current'
hist_date = '2015-21-01'

conn = http.client.HTTPConnection("api.weatherstack.com")
conn.request("GET", f'/{mode}?access_key={key}&query={city}&historical_date={hist_date}')
output = conn.getresponse()
body = output.read()
temperature = "temperature"
print(body)
