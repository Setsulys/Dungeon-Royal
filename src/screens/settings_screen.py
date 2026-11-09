import pygame

from screens.screen import Screen


class SettingsScreen(Screen):

    def handle_events(self, events):

        for event in events:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.game.change_screen("menu")
                    return

    def update(self, dt):
        pass

    def draw(self, screen):

        screen.fill((40, 40, 80))