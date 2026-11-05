import  pygame as py
from screeninfo import get_monitors
from common_tools import GAME_LANGUAGE
from common_tools.managers.text_manager import TextKey

class Screen():
    def __init__(self,height:int=1080):
        self.height = height
        self.width = self.compute_width()

    def compute_width(self):
        return self.height / 9 * 16

    def get_point(self):
        return self.width,self.height


    def icon_and_title():
        py.display.set_caption(GAME_LANGUAGE.get(TextKey.GAME_TITLE))
        game_icon()


    def monitors_info():
        return [m for m in get_monitors()]