from menu_items.menu_item import MenuItem
import platform, os

class ExitItem(MenuItem):


    def start(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        if(platform.system() == 'Windows'):
            os.system('cls')

    def get_name(self):
        return "Exit"

    def get_key_name(self):
        return "e"

    def get_key(self):
        return 'e'
