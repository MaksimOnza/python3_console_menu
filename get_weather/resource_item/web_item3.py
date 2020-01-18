from menu_items.menu_item import MenuItem
from menu import Menu

class WebItem3(MenuItem):

    path = "./data/web.txt"


    def start(self):
        file =  open(self.path, 'w')
        file.write(self.get_name())
        file.close()

    def get_name(self):
        return "WebItem3"

    def get_key_name(self):
        return "3"

    def get_key(self):
        return '3'