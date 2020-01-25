from menu_items.menu_item import MenuItem
import platform, os
from data.key_symbol import KeySymbol

class ExitItem(MenuItem):

    def __init__(self):
        self.__key = KeySymbol()

    def start(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        if(platform.system() == 'Windows'):
            os.system('cls')

    def get_name(self):
        return "Exit"

    def get_key_name(self):
        return self.__key.KEY_EXIT

    def get_key(self):
        return self.__key.KEY_EXIT
