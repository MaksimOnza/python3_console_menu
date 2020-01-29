import os, platform

class ClearDisplay:

    def clear_display(self):
        if(platform.system() == 'Linux'):
            os.system('clear')
        if(platform.system() == 'Windows'):
            os.system('cls')