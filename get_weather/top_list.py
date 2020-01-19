class TopList():

    selected_city = "city not selected"
    selected_web = "web not selected"

    def __init__(self):
        self.selected_city = "city not selected"
        self.selected_web = "web not selected"

    @classmethod 
    def print_web(cls):
        return cls.selected_web

    @classmethod 
    def print_city(cls):
        return cls.selected_city