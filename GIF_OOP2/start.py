from menu import Menu
from menu_items.exit_item import ExitItem
from launch import Launch
from setting_items.setting_item import SettingItem

main_menu = Menu([
	Launch(),
	SettingItem([
		ExitItem(),
				]),
	ExitItem(),
])
main_menu.start()
print()
print("END")


#Закончить менюшку
#chat
#не затягивать
#чтиво документация
#залить на git и сохранять