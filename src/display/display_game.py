import pygame
from pygame.surface import SurfaceType
from math import ceil
from setup import *
from common_tools.managers.text_manager import *
from common_tools.managers.image_manager import Image

HEIGHT_SIZE = 720
FONT_TYPE = "Arial"
FONT_SIZE = ceil(HEIGHT_SIZE / 33)


def display_game():
    window = WindowsSize(HEIGHT_SIZE)

    pygame.init()

    screen = pygame.display.set_mode(window.get_point())
    icon_and_title()
    running=True
    police = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)

    buttons=[TextKey.GAME_MAIN_NEW_GAME,TextKey.GAME_MAIN_LOAD,TextKey.GAME_MAIN_SETTING,TextKey.GAME_MAIN_LEAVE]
    list_rect_buttons=create_buttons(screen,window.width,buttons)
    while running:
        read_image(screen,Image.Player,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        draw_buttons(screen,list(list_rect_buttons),police)
        pygame.display.flip()
    pygame.quit()




############


def create_buttons(screen:SurfaceType,window_width:int,buttons:list[TextKey]):

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
    return zip(list_rects,buttons)


def draw_buttons(screen:SurfaceType, list_rec_buttons:list[tuple[pygame.Rect,TextKey]], police:pygame.font.Font):
    for rect,text in list_rec_buttons:
        text_surface = police.render(texts.get(text),True,(255,255,255))
        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        pygame.draw.rect(screen,(0,128,255),rect,border_radius=5)
        screen.blit(text_surface, text_rect)



# def centering(screen:SurfaceType):
#     rect = rectangle_button()
#     screen_rect = screen.get_rect()
#     rect.center=screen_rect.center
#     pygame.draw.rect(screen,(0,0,255),rect)
#
#
# def rectangle_button():
#     return pygame.Rect(0,0,300,200)



display_game()

