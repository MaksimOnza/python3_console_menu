import http.client
import json
#from pprintpp import pprint
#import requests

key = '719d3fe6203f73509524e0bca348cb53'
city = "kharkiv"
mode = 'current'

conn = http.client.HTTPConnection("api.weatherstack.com")
conn.request("GET", f'/{mode}?access_key={key}&query={city}')
output = conn.getresponse()
body = output.read()
loaded_json = json.loads(body)

print(loaded_json['current']['temperature'])