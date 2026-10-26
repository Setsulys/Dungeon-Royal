# New game
# Load
# Leave

from enum import Enum,auto
import sys
from dungeon.common_tools.text_manager import TextManager
from dungeon.common_tools.input_handler import Input

texts= TextManager("fr")

class MenuType(Enum):
    MAIN_MENU = auto()
    NEW_GAME_MENU = auto()
    LOADING_MENU = auto()
    SETTING_MENU = auto()


class MenuAction(Enum):
    NEW_GAME = auto()
    LOAD = auto()
    SETTING = auto()

class MainMenu():
    def __init__(self):
        self.current_menu = MenuType.MAIN_MENU


    def change_menu(self,):

    def start_game():
        ##
    def load_game():

    def settings():


    def leave_game():
        sys.exit()







def display_confirmation_message():
    return texts.get("game.confirmation_message")


def confirmation_message()->bool:
    return True
    return False
if __name__ == "__main__":
    print(display_confirmation_message())