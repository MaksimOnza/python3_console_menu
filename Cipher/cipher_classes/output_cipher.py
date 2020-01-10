from data.alphabet_morze import AlphabetMorze 

class OutputCipher:

    def __init__(self):
        self.alphabet = AlphabetMorze()


    def output_morze(self, keys, value, bool):
        white = '\033[97m'
        green = '\033[92m'
        word = keys
        word_list = value
        if bool:
            index = 0
            for element in word:
                print(green + word_list[index], end = '')
                index += 1
            print(":" + white)
            index = 0
            for element in word_list:
                print(element + " -> " + word[index])
                index += 1
        else:
            for key in keys:
                print(key + " -> " + self.alphabet.get_symbol(key))