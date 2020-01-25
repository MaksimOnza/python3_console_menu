class TopList():

    selected_city = "city not selected"
    selected_web = "web not selected"

    name = ''
    key = ''
    add_link = ''
    output_param = []
    list_name_param = {}
    param = {}


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
    def get_name(cls):
        return cls.name

    @classmethod 
    def get_key(cls):
        return cls.key

    @classmethod 
    def get_add_link(cls):
        return cls.add_link

    @classmethod 
    def get_output_param(cls):
        return cls.output_param

    @classmethod 
    def get_name_query_city(cls):
        return cls.list_name_param['city']

    @classmethod 
    def get_name_query_key(cls):
        return cls.list_name_param['key']
