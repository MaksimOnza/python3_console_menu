from top_list import TopList

class WriteWebData:

    def __init__(self, data):
        TopList.selected_web = data.get_name()
        TopList.name = data.get_name()
        TopList.key = data.get_key()
        TopList.add_link = data.get_add_link()
        TopList.output_param = data.get_output_param()
        TopList.list_name_param = data.get_list_name_param()