from manag_cashe import ManagCashe


class CacheData:
	
	def __init__(self):
		self.manag_cashe = ManagCashe()

	def set(self, key, data, ttl=5):
		self.manag_cashe.set_cashe(key, data, ttl)

	def get(self, key):
		try:
			return self.manag_cashe.get_cashe(key)
		except:
			return None