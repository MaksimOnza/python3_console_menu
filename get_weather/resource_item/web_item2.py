from menu_items.menu_item import MenuItem
from menu import Menu

class WebItem2(MenuItem):

    path = "./data/web.txt"


    def start(self):
        file =  open(self.path, 'w')
        file.write(self.get_name())
        file.close()

    def get_name(self):
        return "WebItem2"

    def get_key_name(self):
        return "2"

    def get_key(self):
        return '2'