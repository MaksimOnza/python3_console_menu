from data.transit_data import TransitData

class DisplayTopList:

    def __init__(self):
        self.__top_list = TransitData

    def display_top_list(self):
        print(self.__top_list.print_web() + " ------- " + self.__top_list.print_city())
        print("*"*45)