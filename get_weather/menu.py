from clear_display import ClearDisplay
from top_list import TopList

class Menu:
        
    EXIT = 'e'
    __clear = ClearDisplay()
    __top_list = TopList()

    def __init__(self, items):
        self.__items = items
        __key = ''


    def start(self):
        __key = ''
        while __key != self.EXIT:
            self.__clear.clear_display()
            print(self.__top_list.classmethod() + " ------- " + self.__top_list.print_city())
            print("******************")
            for item in self.__items:
                print(item.get_name() + " -> " + item.get_key_name())

            __key = input()
            for item in self.__items:
                if item.get_key() == __key:
                    item.start()