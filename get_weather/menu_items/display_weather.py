from menu_items.menu_item import MenuItem
from menu import Menu

class DisplyWeather(MenuItem):
    
    def __init__(self):
        pass

    def start(self):
        print("DisplyWeather")

    def get_name(self):
        return "DisplyWeather"

    def get_key_name(self):
        return "c"

    def get_key(self):
        return 'c'