import pygame
from screens import Screen


class GameScreen(Screen):

    def handle_events(self, events):

        for event in events:

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    self.game.change_screen("menu")
                    return

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.fill((30, 100, 40))