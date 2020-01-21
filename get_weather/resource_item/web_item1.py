from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList
from data.data_link import DataLink

class WebItem1(MenuItem):

    def __init__(self):
        self.web_name = DataLink()

    def start(self):
        TopList.selected_web = self.get_name()

    def get_name(self):
        return self.web_name.web1

    def get_key_name(self):
        return "1"

    def get_key(self):
        return '1'
