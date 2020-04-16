import time
import csv
import json


class ManagCashe:

	def set_cashe(self, key, data, ttl):
		current_time = float(time.time() + ttl)
		cashe_list = [{'key': key,'data': data, 'expire_time': current_time}]
		with open('cashe.csv', 'w') as f:
			columns = ['key', 'data', 'expire_time']
			writer = csv.DictWriter(f, fieldnames=columns)#, quoting=csv.QUOTE_ALL)
			writer.writeheader()
			writer.writerows(cashe_list)

	def get_cashe(self, key):
		with open('cashe.csv', 'r') as f:
			reader = csv.DictReader(f)
			for row in reader:
					temp = row['data'].replace('\'', '"')
					jsn = json.loads(temp)
					cashe_list = {	
								'temp': jsn['temp'],
								'desc': jsn['desc'],
								}
					return cashe_list
			return None

	def del_cashe(self):
		pass