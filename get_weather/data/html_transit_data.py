class HTMLTransitData:

    selected_city = 'city not selected'
    selected_web = 'web not selected'

    www = ''
    element = ''
    propert = ''
    name_propert = ''

    def __init__(self):
        self.selected_city = "city not selected"
        self.selected_web = "web not selected"

    @classmethod 
    def print_web(cls):
        return cls.selected_web

    @classmethod 
    def print_city(cls):
        return cls.selected_city

    @classmethod 
    def get_www(cls):
        return cls.www

    @classmethod 
    def print_element(cls):
        return cls.element

    @classmethod 
    def print_propert(cls):
        return cls.propert

    @classmethod 
    def get_name_propert(cls):
        return cls.name_propert