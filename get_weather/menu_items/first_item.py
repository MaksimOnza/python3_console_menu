from menu_items.menu_item import MenuItem
from menu import Menu

class StartItem(MenuItem):

    def __init__(self, items):
        self.__first_item_start = Menu(items)

    def start(self):
        self.__first_item_start.start()

    def get_name(self):
        return "StartItem"

    def get_key_name(self):
        return "m"

    def get_key(self):
        return 'm'