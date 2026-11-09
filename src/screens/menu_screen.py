import pygame
from pygame.surface import SurfaceType

from managers import read_image, ImageManager,TextMainButton
from screens import Screen

from config import CONTEXT,FONT_SIZE,FONT_TYPE
from common import create_centered_chained_buttons




class MenuScreen(Screen):
    def __init__(self,game):
        self.game = game
        self.police = pygame.font.SysFont(
            FONT_TYPE,
            FONT_SIZE
        )

        buttons = [
            TextMainButton.NEW_GAME,
            TextMainButton.LOAD,
            TextMainButton.SETTING,
            TextMainButton.LEAVE
        ]

        self.buttons = create_centered_chained_buttons(
            game.screen,
            game.window_size.width,
            buttons
        )

    def handle_events(self,events):
        for event in events:
            button = main_menu_handler(self.buttons,event)

            if button == TextMainButton.NEW_GAME:
                self.game.change_screen("game")
                return
            elif button == TextMainButton.SETTING:
                self.game.change_screen("settings")
                return
            elif button == TextMainButton.LEAVE:
                self.game.running = False
                return

    def update(self,dt):
        pass

    def draw(self,screen):
        read_image(screen, ImageManager.Player,(0,0))
        draw_buttons(screen,self.buttons,self.police)

def main_menu_handler(buttons_position:list[tuple[pygame.Rect,TextMainButton]], event: pygame.event.Event):
    if event.type == pygame.MOUSEBUTTONDOWN:
        for rect,button_name in buttons_position:
            if rect.collidepoint(event.pos):
                return button_name
    return None

def draw_buttons(screen:SurfaceType, list_rec_buttons:list[tuple[pygame.Rect,TextMainButton]], police:pygame.font.Font):
    for rect,text in list_rec_buttons:
        text_surface = police.render(CONTEXT.read(text), True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = rect.center
        pygame.draw.rect(screen,(0,128,255),rect,border_radius=5)
        screen.blit(text_surface, text_rect)
