from data.html_transit_data import HTMLTransitData
from data.transit_data import TransitData
from data.type_web import TypeWeb


class WriteWebData:

    def __init__(self, data):
        self.data = data
        self.type_web = self.data.get_type_web()
        if self.type_web == 'api':
            self.set_transit_data_api()
        elif self.type_web == 'html':
            self.set_transit_data_html()


    def set_transit_data_api(self):
        TypeWeb.type_web = self.type_web
        TransitData.selected_web = self.data.get_name()
        TransitData.name = self.data.get_name()
        TransitData.key = self.data.get_key()
        TransitData.add_link = self.data.get_add_link()
        TransitData.output_param = self.data.get_output_param()
        TransitData.list_name_param = self.data.get_list_name_param()
        

    def set_transit_data_html(self):
        TypeWeb.type_web = self.type_web
        HTMLTransitData.selected_web = self.data.get_www()
        HTMLTransitData.www =  self.data.get_www()
        HTMLTransitData.element = self.data.get_element()
        HTMLTransitData.propert = self.data.get_properties()
        HTMLTransitData.name_propert = self.data.get_name_properties()