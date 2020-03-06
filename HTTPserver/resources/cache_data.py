import time


class CacheData:
	

	kesh_dict = {}

	def delta_time(self):
		if((time.time() - self.kesh_dict['time']) < 3600):
			return True
		else:
			return False
	
	def check_cache(self, resource_city):
		if(resource_city in self.kesh_dict):
			if(self.delta_time()):
				return True
			else:
				return False
		else:
			return False

