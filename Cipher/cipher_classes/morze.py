from data.alphabet_morze import AlphabetMorze 
from cipher_classes.general_cipher import GeneralCipher
from cipher_classes.output_cipher import OutputCipher

class Morze(GeneralCipher):

    def __init__(self):
        self.__crypt = []
        self.__decrypt = []
        self.alphabet = AlphabetMorze()
        self.output = OutputCipher()

    def coder(self, word):
        word_items = word.split()
        word_list = word
        for word_item in word_items:
            for symbol in word_item:
                self.__crypt.append(self.alphabet.get_symbol(symbol.swapcase()))
            self.output.output_morze(self.__crypt, word_item, True)
            self.__crypt.clear()
        input()

    def decoder(self, keys):
        key_items = keys.split()
        for key_item in key_items:
            self.__decrypt.append(self.alphabet.get_key(key_item))
        self.output.output_morze(self.__decrypt, key_items, False)
        self.__decrypt.clear()
        input()
        
