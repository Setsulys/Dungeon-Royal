import pygame
from enum import Enum,auto

from dataclasses import dataclass
class Input(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()
    CONFIRM = auto()
    CANCEL = auto()

@dataclass(frozen=False)
class InputHandler:
    def __init__(self):
        self.actions={
            pygame.K_UP: Input.UP,
            pygame.K_DOWN: Input.DOWN,
            pygame.K_LEFT: Input.LEFT,
            pygame.K_RIGHT: Input.RIGHT,
            pygame.K_z: Input.UP,
            pygame.K_s: Input.DOWN,
            pygame.K_q: Input.LEFT,
            pygame.K_d: Input.RIGHT,
            pygame.K_RETURN: Input.CONFIRM,
            pygame.K_ESCAPE: Input.CANCEL,
        }

    def handle_event(self,event):
        if event.type==pygame.KEYDOWN:
            return self.actions.get(event.key)
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button ==1:
                return Input.CONFIRM
            if event.button==3:
                return Input.CANCEL

        return None