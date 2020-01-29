from menu import Menu
from menu_items.menu_item import MenuItem

class WebSelectItem(MenuItem):

    def __init__(self, items):
        self.__name = "WebSelect"
        self.__second_menu = Menu(items)

    def start(self):
        self.__second_menu.start()

    def get_name(self):
        return self.__name

    def get_key_name(self):
        return "w"

    def get_key(self):
        return 'w'