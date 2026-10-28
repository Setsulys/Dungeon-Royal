import pygame
from enum import  Enum
from common_tools.managers.ressource_path import RESOURCES_DIR

IMAGES_DIR = RESOURCES_DIR / "images"


class Image(Enum):
    Player="Player.png"

def game_icon():
    file = IMAGES_DIR / Image.Player.value
    image = pygame.image.load(str(file)).convert()
    pygame.display.set_icon(image)


def read_image(screen,image_name:Image,position:tuple[int,int]):
    file = IMAGES_DIR / image_name.value
    image = pygame.image.load(str(file)).convert()
    screen.blit(image,position)

