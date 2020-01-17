
main_menu = Menu([
    StartItem(
    	[
        ResourceSelection(
        	[
        	CitySelection(),
        	MultyCitySelection(),
        	ExitItem()
        	])
        ]),
    ExitItem()
])
main_menu.start()