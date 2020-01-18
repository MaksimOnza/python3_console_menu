from menu_items.menu_item import MenuItem
from menu import Menu

class WebItem1(MenuItem):

    def __init__(self):
        pass

    def start(self):
        self.__start.start()

    def get_name(self):
        return "WebItem1"

    def get_key_name(self):
        return "1"

    def get_key(self):
        return '1'