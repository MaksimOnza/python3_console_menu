from top_list import TopList

class DisplayTopList:

    def __init__(self):
        self.__top_list = TopList()

    def display_top_list(self):
        print(self.__top_list.print_web() + " ------- " + self.__top_list.print_city())
        print("******************")