
from pygame.surface import SurfaceType


from setup import *

from common_tools.managers.image_manager import Image


from common_tools.common_tools import create_centered_chained_buttons
from common_tools.global_elements import *




def display_game():
    window = WindowsSize(HEIGHT_SIZE)

    pygame.init()

    screen = pygame.display.set_mode(window.get_point())
    icon_and_title()
    running=True
    police = pygame.font.SysFont(FONT_TYPE, FONT_SIZE)

    buttons=[TextMainButton.NEW_GAME,TextMainButton.LOAD,TextMainButton.SETTING,TextMainButton.LEAVE]
    list_rect_buttons=create_centered_chained_buttons(screen,window.width,buttons)
    while running:
        read_image(screen,Image.Player,(0,0))
        for event in pygame.event.get():
            event_handler = main_menu_handler(list_rect_buttons,event)
            if event_handler != None:
                print(text_manager.get(event_handler))
            if event_handler == TextMainButton.LEAVE:
                running=False
        draw_buttons(screen,list_rect_buttons,police)
        pygame.display.flip()
    pygame.quit()

############

def main_menu_handler(buttons_position:list[tuple[pygame.Rect,TextMainButton]], event: pygame.event.Event):
    if event.type == pygame.QUIT:
        return TextMainButton.LEAVE
    if event.type == pygame.MOUSEBUTTONDOWN:
        pos_x,pos_y=pygame.mouse.get_pos()
        for rect,button_name in buttons_position:
            button_top_x,button_top_y= rect.topleft
            button_bottom_x,button_bottom_y=rect.bottomright
            if button_top_x <= pos_x <= button_bottom_x and button_top_y <= pos_y <= button_bottom_y:
                return button_name
    return None







def draw_buttons(screen:SurfaceType, list_rec_buttons:list[tuple[pygame.Rect,TextMainButton]], police:pygame.font.Font):
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

