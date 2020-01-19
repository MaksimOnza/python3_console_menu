from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList

class WebItem2(MenuItem):

    def start(self):
        TopList.selected_web = self.get_name()

    def get_name(self):
        return "WebItem2"

    def get_key_name(self):
        return "2"

    def get_key(self):
        return '2'