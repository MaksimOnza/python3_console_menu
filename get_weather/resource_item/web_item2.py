from menu_items.menu_item import MenuItem
from menu import Menu
from data.web2 import Web2
from data.write_web_data import WriteWebData
from data.key_symbol import KeySymbol

class WebItem2(MenuItem):

    def __init__(self):
        self.web_data = Web2()
        self.__key = KeySymbol()

    def start(self):
        WriteWebData(self.web_data)

    def get_name(self):
        return self.web_data.name

    def get_key_name(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]

    def get_key(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]