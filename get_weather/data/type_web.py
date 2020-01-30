class TypeWeb:

    type_web = ''
    type_html = 'html'
    type_api = 'api'
    selected_city = "city not selected"
    selected_web = "web not selected"

    @classmethod 
    def set_type_web(cls, type_web):
        cls.type_web = type_web

    @classmethod 
    def get_type_web(cls):
        return cls.type_web

    @classmethod 
    def print_web(cls):
        return cls.selected_web

    @classmethod 
    def print_city(cls):
        return cls.selected_city