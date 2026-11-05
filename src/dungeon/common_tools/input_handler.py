import pygame
from enum import Enum,auto

class Input(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CONFIRM = auto()
    CANCEL = auto()

class InputHandler:
    def __init__(self):
        self.actions={
            pygame.K_UP: Input.UP,
            pygame.K_DOWN: Input.DOWN,
            pygame.K_LEFT: Input.LEFT,
            pygame.K_RIGHT: Input.RIGHT,
            pygame.K_z: Input.UP,
            pygame.K_s: Input.DOWN,
            pygame.K_q: Input.RIGHT,
            pygame.K_d: Input.LEFT,
            pygame.K_RETURN: Input.CONFIRM,
            pygame.K_ESCAPE: Input.CANCEL,
        }

    def handle_event(self,event):
        if event.type!=pygame.KEYDOWN:
            return None
        return self.actions.get(event.key)
