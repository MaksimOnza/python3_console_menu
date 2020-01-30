from menu import Menu
from menu_items.city_item import CityItem
from menu_items.exit_item import ExitItem
from menu_items.web_select_item import WebSelectItem
from menu_items.weatherstack_item import WeatherstackItem
from menu_items.openweathermap_item import OpenweathermapItem
from menu_items.worldweatheronline_item import WorldweatheronlineItem
from menu_items.sinoptyk_item import SinoptykItem
from display.show_weather import ShowWeather
from menu_items.show_weather_item import ShowWeatherItem
from data.type_web import TypeWeb



main_menu = Menu([
    WebSelectItem([
        WeatherstackItem(),
        OpenweathermapItem(),
        WorldweatheronlineItem(),
        SinoptykItem(),
        ExitItem()
            ]),
    CityItem(),
    ShowWeatherItem(),
    ExitItem()
    ])
main_menu.start()