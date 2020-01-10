from menu_items.menu_item import MenuItem
from morze.morze import Morze

class CoderMorze(MenuItem):
    
    def __init__(self):
        self.__morze = Morze()

    def start(self):
        word = input()
        self.__morze.coder(word)


    def get_name(self):
        return "Coder"

    def get_key_name(self):
        return "c"

    def get_key(self):
        return 'c'