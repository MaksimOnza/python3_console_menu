from clear_display import ClearDisplay

class Menu:
        
    EXIT = 'e'
    __clear = ClearDisplay()

    def __init__(self, items):
        self.__items = items
        __key = ''


    def start(self):
        __key = ''
        while __key != self.EXIT:
            self.__clear.clear_display()
            for item in self.__items:
                print(item.get_name() + " -> " + item.get_key_name())

            __key = input()
            for item in self.__items:
                if item.get_key() == __key:
                    item.start()