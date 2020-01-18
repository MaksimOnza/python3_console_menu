from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList

class WebItem1(MenuItem):

    path = "./data/web.txt"

    def __init__(self):
        self.var = TopList()

    def start(self):
        #file =  open(self.path, 'w')
        #file.write(self.get_name())
        #file.close()
        self.test_var()

    def get_name(self):
        return "WebItem1"

    def get_key_name(self):
        return "1"

    def get_key(self):
        return '1'

    def test_var(self):
        self.var.experement_var = self.get_name()