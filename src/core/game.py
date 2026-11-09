import pygame
from screens import MenuScreen,GameScreen,SettingsScreen

from config import HEIGHT_SIZE,WindowsSize,icon_and_title

from enum import Enum

class Screen_names(Enum):
    MAIN_MENU = "menu"
    GAME = "game"
    LOAD = "load"
    SETTING = "setting"


class Game:

    def __init__(self):
        pygame.init()

        self.window_size = WindowsSize(HEIGHT_SIZE)

        self.screen = pygame.display.set_mode(
            self.window_size.get_point()
        )

        icon_and_title()

        self.clock = pygame.time.Clock()
        self.running = True

        self.screens = {
            "menu": MenuScreen(self),
            "game": GameScreen(),
            # "load": LoadScreen(self),
            "settings": SettingsScreen()
        }

        self.current_screen = self.screens["menu"]

    def change_screen(self,screen_name):
        if screen_name not in self.screens:
            raise ValueError(f"Unknown Screen:{screen_name}")
        new_screen = self.screens[screen_name]

        if new_screen is self.current_screen:
            return
        self.current_screen.on_exit()
        self.current_screen = new_screen
        self.current_screen.on_enter()



    def run(self):
        while self.running:
            dt = self.clock.tick(60) / 1000

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT:
                    self.running = False

            if not self.running:
                break

            self.current_screen.handle_events(events)
            self.current_screen.update(dt)
            self.current_screen.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
