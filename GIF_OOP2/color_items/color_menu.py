class ColorMenu:

    Red = '\033[91m'
    Green = '\033[92m'
    Yellow = '\033[93m'
    Blue = '\033[94m'
    Magenta = '\033[95m'
    Cyan = '\033[96m'
    White = '\033[97m'
    Grey = '\033[90m'

    dict_color2= {
                "Red":'\033[91m',
                "Green":'\033[92m',
                "Yellow":'\033[93m',
                "Blue":'\033[94m',
                "Magenta":'\033[95m',
                "Cyan":'\033[96m',
                "White":'\033[97m',
                "Grey":'\033[90m'
                }

    dict_color = {
                1:Red,
                2:Green,
                3:Yellow,
                4:Blue,
                5:Magenta,
                6:Cyan,
                7:White,
                8:Grey
                }

    #def __init__(self):
        #self.__items = items

    def start(self):
        j = 1
        for color in self.dict_color2:
            print(self.dict_color2[color] + color + " -> " + str(j))
            j+=1
        col = input()
        print(self.dict_color[int(col)])
        j = 0


    def get_name(self):
        return "Select Color"


    def get_key_name(self):
        return 'c'


    def get_key(self):
        return 'c'