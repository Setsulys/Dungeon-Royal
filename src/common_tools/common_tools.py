import pygame
from pygame.surface import SurfaceType

from configuration import config

from common_tools.managers.text_manager import TextMainButton

def create_centered_chained_buttons(screen:SurfaceType,window_width:int,buttons:list[TextMainButton]):

    button_width= window_width /10
    button_height = config.HEIGHT_SIZE / 10
    spacing = window_width/100
    screen_rect = screen.get_rect()

    button_nb = len(buttons)
    total_bloc_size = (button_nb * button_height) + ((button_nb-1)*spacing)
    y_start = (config.HEIGHT_SIZE - total_bloc_size) //2
    list_rects=[]
    for i in range(button_nb):
        y_position = y_start + i * (button_height+spacing)
        rect = pygame.Rect(0,y_position,button_width,button_height)
        rect.centerx = screen_rect.centerx
        list_rects.append(rect)
    return list(zip(list_rects,buttons))