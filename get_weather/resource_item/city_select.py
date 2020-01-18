from menu_items.menu_item import MenuItem
from menu import Menu

class City(MenuItem):
    
    def __init__(self, items):
        pass

    def start(self):
        print("CitySelection")

    def get_name(self):
        return "CitySelection"

    def get_key_name(self):
        return "c"

    def get_key(self):
        return 'c'