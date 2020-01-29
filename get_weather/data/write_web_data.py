from data.transit_data import TransitData

class WriteWebData:

    def __init__(self, data):
        TransitData.type_web =  data.get_type_web()
        TransitData.selected_web = data.get_name()
        TransitData.name = data.get_name()
        TransitData.key = data.get_key()
        TransitData.add_link = data.get_add_link()
        TransitData.output_param = data.get_output_param()
        TransitData.list_name_param = data.get_list_name_param()