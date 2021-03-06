from menu import Menu
from menu_items.exit_item import ExitItem
from menu_items.launch_item import LaunchItem
from menu_items.display_item import DisplayItem
from setting_items.setting_item import SettingItem
from setting_items.color_item import ColorItem
from setting_items.speed_item import SpeedItem
from color_items.color_select import ColorSelect


main_menu = Menu([
    LaunchItem(),
    DisplayItem(),
    SettingItem([
        ColorItem([
            ColorSelect(),
            ExitItem(),
            ]),
        SpeedItem(),
        ExitItem(),
                ]),
    ExitItem(),
])
main_menu.start()
