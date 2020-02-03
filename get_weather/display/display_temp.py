from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.type_web import TypeWeb
 
class DisplayTemp:

    __KELVIN = 273
    __TEMP_POINT = 200
    __DEGREE_SIGN = u'\xb0'
    __CELSIY_SYGN = 'C'

    def __init__(self, web, json):
        self.__web = web
        if TypeWeb.get_type_web() == 'api':
            self.respons_param = TransitData
        elif TypeWeb.get_type_web() == 'html':
            self.respons_param = HTMLTransitData
        self.display_json_data(json)


    def display_json_data(self, loaded_json):
        try:
            for iter in self.respons_param.output_param:
                temp = loaded_json[iter]
                loaded_json = temp
            if int(loaded_json) > self.__TEMP_POINT:
                print("%.2f"%(loaded_json - self.__KELVIN), self.__DEGREE_SIGN, end='')
                print(self.__CELSIY_SYGN)
            else:
                print(loaded_json, self.__DEGREE_SIGN, end='' )
                print(self.__CELSIY_SYGN)
        except:
            print('Somsing wrong, maybe city?')

    #def display(self, loaded_json):
        #for param in self.respons_param:
         #   print()