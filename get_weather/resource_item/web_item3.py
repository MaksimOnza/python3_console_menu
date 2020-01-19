from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList

class WebItem3(MenuItem):

    def start(self):
        TopList.selected_web = self.get_name()

    def get_name(self):
        return "WebItem3"

    def get_key_name(self):
        return "3"

    def get_key(self):
        return '3'