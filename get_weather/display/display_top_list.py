from data.transit_data import TransitData
from data.html_transit_data import HTMLTransitData
from data.type_web import TypeWeb

class DisplayTopList:

    def __init__(self):
        if TypeWeb.get_type_web() == 'api':
            self.__top_list = TransitData
        elif TypeWeb.get_type_web() == 'html':
            self.__top_list = HTMLTransitData
        else:
            self.__top_list = HTMLTransitData
        

    def display_top_list(self):
        print(self.__top_list.print_web() + " ------- " + self.__top_list.print_city())
        print("*"*45)