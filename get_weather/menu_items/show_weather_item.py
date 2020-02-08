from menu_items.menu_item import MenuItem

class ShowWeatherItem(MenuItem):

    def __init__(self, state, resources):
        self.__resources = resources
        self.__state = state

    def start(self):
        try:
            resource = self.__resources[self.__state.resource]
            temperature = resource.get_temperature(self.__state.city)

            print(f'{temperature} C')
            input()
        except Exception as e:
            print(e)
            print('Press any key')
            input()

    def get_name(self):
        return "ShowTemperature"

    def get_key_name(self):
        return "s"

    def get_key(self):
        return 's'