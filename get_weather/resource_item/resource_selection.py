from menu import Menu
from menu_items.menu_item import MenuItem
from display.display_resource import DisplayResource

class ResourceSelection(MenuItem):

    def __init__(self, items):
        self.__first_item = "first_item"
        self.__display_start = DisplayResource(self.__first_item)
        print()
        self.__first_item_start = Menu(items)
        input()

    def start(self):
        self.__display_start.start()
        self.__first_item_start .start()

    def get_name(self):
        return "ResourceSelection"

    def get_key_name(self):
        return "m"

    def get_key(self):
        return 'm'