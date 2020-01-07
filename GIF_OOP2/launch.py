from menu_items.menu_item import MenuItem

class Launch(MenuItem):
    def start(self):
        print("Start")

    def get_name(self):
        return "Start"

    def get_key_name(self):
        return "Enter"

    def get_key(self):
        return ''