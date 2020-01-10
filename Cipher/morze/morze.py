from data.alphabet_morze import AlphabetMorze 

class Morze:

    def __init__(self):
        self.__crypt = []
        self.__decrypt = []
        self.alphabet = AlphabetMorze()

    def coder(self, word):
        word_items = word.split()
        word_list = word
        for word_item in word_items:
            for symbol in word_item:
                self.__crypt.append(self.alphabet.get_symbol(symbol.swapcase()))
            self.output(self.__crypt, word_item)
            self.__crypt.clear()
        input()

    def decoder(self, keys):
        key_items = keys.split()
        for key_item in key_items:
            self.__decrypt.append(self.alphabet.get_key(key_item))
        self.output2(self.__decrypt, key_items)
        self.__decrypt.clear()
        input()
        
    def output2(self, keys, value):
        white = '\033[97m'
        green = '\033[92m'
        for key in keys:
            print(key + " -> " + self.alphabet.get_symbol(key))

    def output(self, word, word_list):
        #add clearing display
        white = '\033[97m'
        green = '\033[92m'
        index = 0
        for element in word:
            print(green + word_list[index], end = '')
            index += 1
        print(":" + white)
        index = 0
        for element in word:
            print(word_list[index] + " -> " + element)
            index += 1