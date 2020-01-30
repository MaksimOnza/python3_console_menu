from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.type_web import TypeWeb

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
        print(self.__top_list.print_web() + " ------- " + self.__top_list.print_city())
        print("*"*45)