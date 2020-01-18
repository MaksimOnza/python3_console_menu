from menu import Menu
from menu_items.menu_item import MenuItem
from display.display_resource import DisplayResource

class WebSelect(MenuItem):

    def __init__(self, items):
        self.__first_item = "first_item"
        self.__first_item_start = Menu(items)

    def start(self):
        self.__first_item_start .start()

    def get_name(self):
        return "WebSelect"

    def get_key_name(self):
        return "m"

    def get_key(self):
        return 'm'