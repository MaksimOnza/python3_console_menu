from menu import Menu
from menu_items.first_item import StartItem
from resource_item.resource_selection import ResourceSelection
from resource_item.city_selection import City
from menu_items.exit_item import ExitItem
from resource_item.web_item1 import WebItem1
from resource_item.web_item2 import WebItem2
from resource_item.web_item3 import WebItem3

main_menu = Menu([
    StartItem([
        ResourceSelection([
        	WebItem1(),
        	WebItem2(),
        	WebItem3(),
        	ExitItem()
        	]),
        City([
        	#CitySelection(),
        	#MultyCitySelection(),
        	ExitItem()
        	])
        ]),
    ExitItem()
])
main_menu.start()