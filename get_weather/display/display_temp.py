from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.type_web import TypeWeb
 
class DisplayTemp:

    def __init__(self, web):
        self.__web = web
        if TypeWeb.get_type_web() == 'api':
            self.respons_param = TransitData
        elif TypeWeb.get_type_web() == 'html':
            self.respons_param = HTMLTransitData
       

    def display_json_data(self, loaded_json):
        for iter in self.respons_param.output_param:
            temp = loaded_json[iter]
            loaded_json = temp
        if int(loaded_json) > 200:
            print("%.2f"%(loaded_json - 273))
        else:
            print(loaded_json)

    def display(self, loaded_json):
        for param in self.respons_param:
            print()