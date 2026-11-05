import pygame
from pygame.surface import SurfaceType

from dungeon.generator.maze_generation import Cell,CellType
from common_tools.global_elements import *

def remaining_cell_type(dungeon: list[list[Cell]],cell_type:CellType):
    return [(i, j) for i, row in enumerate(dungeon) for j, cell in enumerate(row) if cell.type == cell_type]



def create_centered_chained_buttons(screen:SurfaceType,window_width:int,buttons:list[TextMainButton]):

    button_width= window_width /10
    button_height = HEIGHT_SIZE / 10
    spacing = window_width/100
    screen_rect = screen.get_rect()

    button_nb = len(buttons)
    total_bloc_size = (button_nb * button_height) + ((button_nb-1)*spacing)
    y_start = (HEIGHT_SIZE - total_bloc_size) //2
    list_rects=[]
    for i in range(button_nb):
        y_position = y_start + i * (button_height+spacing)
        rect = pygame.Rect(0,y_position,button_width,button_height)
        rect.centerx = screen_rect.centerx
        list_rects.append(rect)
    return list(zip(list_rects,buttons))