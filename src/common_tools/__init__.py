from . import common_tools
from . import input_handler


__all__=["common_tools","input_handler","HEIGHT_SIZE","FONT_TYPE","FONT_SIZE","GAME_LANGUAGE"]

from math import ceil
from . managers.text_manager import TextManager,TextLanguage

HEIGHT_SIZE = 720
FONT_TYPE = "Arial"
FONT_SIZE = ceil(HEIGHT_SIZE / 33)


GAME_LANGUAGE = TextManager(TextLanguage.FR)

