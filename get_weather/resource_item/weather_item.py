from menu_items.menu_item import MenuItem
from menu import Menu
from top_list import TopList
from display.show_weather import ShowWeather

class WeatherItem(MenuItem):

    def start(self):
        s = ShowWeather()
        s.show_weather()
        input()

    def get_name(self):
        return "WeatherItem"

    def get_key_name(self):
        return "s"

    def get_key(self):
        return 's'