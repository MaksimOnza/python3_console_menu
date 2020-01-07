from menu_items.menu_item import MenuItem
import platform, os

class ExitItem(MenuItem):
    __count = 2
    
    def __init__(self):
        self.__count += 1

    def count_fun(self):
        return self.__count

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
