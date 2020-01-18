class TopList():

    path_web = "./data/web.txt"
    path_city = "./data/city.txt"
    text_web = ""
    text_city = ""

    def __init__(self):
        self.selected_city = "city not selected"
        self.selected_web = "web not selected"
        self.experement_var = ""

    
    def print_web(self):
        with open(self.path_web) as file_top_list:
            for line in file_top_list:
                self.text_web = line
        if self.text_web == "":
            return self.selected_web
        else:
            return self.text_web

    def print_city(self):
        with open(self.path_city) as file_top_list:
            for line in file_top_list:
                self.text_city = line
        if self.text_city == "":
            return self.selected_city
        else:
            return self.text_city

    @classmethod
    def classmethod(cls):
        return cls.experement_var