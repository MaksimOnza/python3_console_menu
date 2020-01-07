import platform, os

class Menu:
        
    EXIT = 'e'

    def __init__(self, items):
        self.__items = items
        __key = ''


    def start(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        if(platform.system() == 'Windows'):
            os.system('cls')
        __key = ''
        while __key != self.EXIT:
            for item in self.__items:
                print(item.get_name() + " -> " + item.get_key_name())

            __key = input()
            for item in self.__items:
                if item.get_key() == __key:
                    item.start()
