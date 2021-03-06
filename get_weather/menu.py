from display.clear_display import ClearDisplay
from display.display_top_list import DisplayTopList
from data.key_symbol import KeySymbol
import logging
import shutil

logging.basicConfig(filename="sample.log", level=logging.INFO)

class Menu:
        
    __clear = ClearDisplay()
    __top_list = DisplayTopList()

    def __init__(self, items):
        self.__key = KeySymbol()
        self.__items = items

    def start(self):
        width = int(self.get_termwidth()/2)-8
        key = ''
        while key != self.__key.KEY_EXIT:
            self.__clear.clear_display()
            self.__top_list.display_top_list()
            for item in self.__items:
                print(' ' * width + item.get_name() + " -> " + item.get_key_name())

            key = input()
            for item in self.__items:
                if item.get_key() == key:
                    item.start()

    def get_termwidth(self, default=None):
        return shutil.get_terminal_size((default, default)).columns