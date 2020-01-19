from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList

class CitySelect(MenuItem):

    def start(self):
        print("Enter the City or town")
        enter_city = input()
        TopList.selected_city = enter_city

    def get_name(self):
        return "CitySelect"

    def get_key_name(self):
        return "c"

    def get_key(self):
        return 'c'