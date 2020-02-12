from menu import Menu
from menu_items.city_item import CityItem
from menu_items.exit_item import ExitItem
from menu_items.web_select_item import WebSelectItem
from menu_items.weatherstack_item import WeatherstackItem
from menu_items.openweathermap_item import OpenweathermapItem
from menu_items.worldweatheronline_item import WorldweatheronlineItem
from menu_items.sinoptyk_item import SinoptykItem
from menu_items.show_weather_item import ShowWeatherItem
from state import State
from resources.openweathermap import OpenweathermapResource
from resources.weatherstack import WeatherstackResource
from resources.worldweatheronline import WorldweatheronlineResource
from resources.sinoptik import SinoptikResource
import config


state = State()


resources = {
    'Weatherstack': WeatherstackResource(config.WEATHERSTACK_ACCESS_KEY),
    'Openweathermap': OpenweathermapResource(config.OPENWEATHERMAP_ACCESS_KEY),
    'Worldweatheronline': WorldweatheronlineResource(config.WORLDWEATHERONLINE_ACCESS_KEY),
    'Sinoptik': SinoptikResource()
}

main_menu = Menu([
    WebSelectItem([
        WeatherstackItem(state),
        OpenweathermapItem(state),
        WorldweatheronlineItem(state),
        SinoptykItem(state),
        ExitItem()
    ]),
    CityItem(state),
    ShowWeatherItem(state, resources),
    ExitItem()
])
main_menu.start()


#провайдер возвращает все в цельсиях
#почистить лишнее
#пофиксить провайдеров
#сделать возврат температуры в браузере и в json