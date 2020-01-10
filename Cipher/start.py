from menu import Menu
from menu_items.morze_item import MorzeItem
from menu_items.ceaser_item import CeaserItem
from menu_items.exit_item import ExitItem
from coder_items.coder_morze import CoderMorze
from coder_items.decoder_morze import DecoderMorze

main_menu = Menu([
    MorzeItem([
        CoderMorze(),
        DecoderMorze(),
        ExitItem()
        ]),
    CeaserItem([
        CoderMorze(),
        DecoderMorze(),
        ExitItem()
        ]),
    ExitItem()
])
main_menu.start()