import pygame
from enum import  Enum
from managers import RESOURCES_DIR

IMAGES_DIR = RESOURCES_DIR / "images"


class ImageManager(Enum):
    Player="Player.png"

def game_icon():
    file = IMAGES_DIR / ImageManager.Player.value
    image = pygame.image.load(str(file)).convert()
    pygame.display.set_icon(image)


def read_image(screen, image_name:ImageManager, position:tuple[int,int]):
    file = IMAGES_DIR / image_name.value
    image = pygame.image.load(str(file)).convert()
    screen.blit(image,position)

