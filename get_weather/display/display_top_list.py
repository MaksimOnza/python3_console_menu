from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.type_web import TypeWeb
import shutil

class DisplayTopList:

    def __init__(self):
        self.__top_list = TypeWeb
        self.type_web = ''
        

    def check_type_web(self):
        self.type_web = TypeWeb.get_type_web()
        if self.type_web == TypeWeb.type_api:
            self.__top_list = TransitData
        elif self.type_web == TypeWeb.type_html:
            self.__top_list = HTMLTransitData

    def display_top_list(self):
        self.check_type_web()
        width = int(self.get_termwidth()/2)-20
        print(' ' * width + self.__top_list.print_web() + " ------- " + TypeWeb.print_city())
        print(' ' * width + "*"*45)

    def get_termwidth(self, default=None):
        return shutil.get_terminal_size((default, default)).columns