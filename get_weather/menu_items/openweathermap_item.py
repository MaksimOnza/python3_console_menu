from menu_items.menu_item import MenuItem
from data.type_web import TypeWeb
from data.openweathermap_data import OpenweathermapData
from data.write_web_data import WriteWebData
from data.key_symbol import KeySymbol

class OpenweathermapItem(MenuItem):

    def __init__(self):
        self.web_data = OpenweathermapData()
        TypeWeb.set_type_web(self.web_data.type_web)
        self.__key = KeySymbol()

    def start(self):
        WriteWebData(self.web_data)

    def get_name(self):
        return self.web_data.name

    def get_key_name(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]

    def get_key(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]