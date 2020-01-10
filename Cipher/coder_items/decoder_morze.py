from menu_items.menu_item import MenuItem
from cipher_classes.morze import Morze

class DecoderMorze(MenuItem):
    
    def __init__(self):
        self.__morze = Morze()

    def start(self):
        word = input()
        self.__morze.decoder(word)

    def get_name(self):
        return "Decoder"

    def get_key_name(self):
        return "d"

    def get_key(self):
        return 'd'


