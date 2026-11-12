import pygame
from math import ceil
from screeninfo import get_monitors

from config import GameContext
from managers import TextKey
from managers import game_icon

HEIGHT_SIZE = 720
FONT_TYPE = "Arial"
FONT_SIZE = ceil(HEIGHT_SIZE / 33)

CONTEXT = GameContext()

class WindowsSize:
    def __init__(self,height:int=1080):
        self.height = height
        self.width = self.compute_width()

    def compute_width(self):
        return self.height / 9 * 16

    def get_point(self):
        return self.width,self.height


def icon_and_title():
    pygame.display.set_caption(CONTEXT.read(TextKey.GAME_TITLE))
    game_icon()


def monitors_info():
    return [m for m in get_monitors()]