from menu_items.menu_item import MenuItem
from menu import Menu

class WebItem2(MenuItem):

    def __init__(self):
        pass

    def start(self):
        self.__start.start()

    def get_name(self):
        return "WebItem2"

    def get_key_name(self):
        return "2"

    def get_key(self):
        return '2'