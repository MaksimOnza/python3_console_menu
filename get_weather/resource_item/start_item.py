from menu_items.menu_item import MenuItem
from menu import Menu

class StartItem(MenuItem):

    def __init__(self, items):
        self.__start = Menu(items)

    def start(self):
        self.__start.start()

    def get_name(self):
        return "Start"

    def get_key_name(self):
        return "s"

    def get_key(self):
        return 's'