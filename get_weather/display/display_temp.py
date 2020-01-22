from data.data_link import DataLink


class DisplayTemp:

    def __init__(self, web):
        self.web_obj = DataLink()
        self.__web = web
        self.__first_level = self.web_obj.query_link['first_level'][self.__web]
        self.__second_level = self.web_obj.query_link['second_level'][self.__web]
        self.__third_level = self.web_obj.query_link['third_level'][self.__web]
        self.__fourth_level = self.web_obj.query_link['fourth_level'][self.__web]

    def display_json_data(self, loaded_json):
        try:
            if self.__web == self.web_obj.dic_web_key[1]:
                print("%.2f"%(loaded_json[self.__first_level][self.__second_level]-273))
            elif self.__web == self.web_obj.dic_web_key[2]:
                print(loaded_json[self.__first_level][self.__second_level][self.__third_level][self.__fourth_level])
            elif self.__web == self.web_obj.dic_web_key[0]:
                print(loaded_json[self.__first_level][self.__second_level])
        except:
            print("Wron enterd city or town")
            print("Try again")
