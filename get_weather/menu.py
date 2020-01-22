from clear_display import ClearDisplay
from display.display_top_list import DisplayTopList

class Menu:
        
    EXIT = 'e'
    __clear = ClearDisplay()
    __top_list = DisplayTopList()

    def __init__(self, items):
        self.__items = items
        __key = ''


    def start(self):
        __key = ''
        while __key != self.EXIT:
            self.__clear.clear_display()
            self.__top_list.display_top_list()
            for item in self.__items:
                print(item.get_name() + " -> " + item.get_key_name())

            __key = input()
            for item in self.__items:
                if item.get_key() == __key:
                    item.start()