from data.data_link import DataLink
from top_list import TopList
 
class DisplayTemp:

    def __init__(self, web):
        self.respons_param = TopList
        self.web_obj = DataLink()
        self.__web = web

    def display_json_data(self, loaded_json):
        for iter in self.respons_param.output_param:
            temp = loaded_json[iter]
            loaded_json = temp
        if loaded_json > 200:
            print("%.2f"%(loaded_json - 273))
        else:
            print(loaded_json)

    def display(self, loaded_json):
        for param in self.respons_param:
            print()