from menu import Menu
from resource_item.city_select import CitySelect
from menu_items.exit_item import ExitItem
from resource_item.web_select import WebSelect
from resource_item.web_item1 import WebItem1
from resource_item.web_item2 import WebItem2
from resource_item.web_item3 import WebItem3
from display.show_weather import ShowWeather
from resource_item.weather_item import WeatherSelect



main_menu = Menu([
    WebSelect([
        WebItem1(),
        WebItem2(),
        WebItem3(),
        ExitItem()
            ]),
    CitySelect(),
    WeatherSelect(),
    ExitItem()
    ])
main_menu.start()