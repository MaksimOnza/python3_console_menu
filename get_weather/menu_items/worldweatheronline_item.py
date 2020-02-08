from menu_items.menu_item import MenuItem
from data.key_symbol import KeySymbol

class WorldweatheronlineItem(MenuItem):
    __key = KeySymbol()

    def __init__(self, state):
        self.__state = state

    def start(self):
        self.__state.resource = self.get_name()

    def get_name(self):
        return 'Worldweatheronline'

    def get_key_name(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]

    def get_key(self):
        return self.__key.DICT_KEY_WEB[self.get_name()]