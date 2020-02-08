import shutil

class DisplayTopList:

        
    def display_top_list(self):
        width = int(self.get_termwidth()/2)-20
        print(' ' * width + "*"*45)

    def get_termwidth(self, default=None):
        return shutil.get_terminal_size((default, default)).columns