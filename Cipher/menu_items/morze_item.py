from menu_items.menu_item import MenuItem
from menu import Menu

class MorzeItem(MenuItem):

    def __init__(self, items):
        self.__morze_start = Menu(items)

    def start(self):
        self.__morze_start.start()

    def get_name(self):
        return "Morze"

    def get_key_name(self):
        return "m"

    def get_key(self):
        return 'm'