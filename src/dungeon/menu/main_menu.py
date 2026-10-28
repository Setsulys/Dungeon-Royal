# New game
# Load
# Leave

from enum import Enum,auto
import sys
from common_tools.managers.text_manager import TextManager,TextKey

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


class SaveSlot():
    pass


class MainMenu():
    pass
    # def __init__(self):
    #     self.current_menu = MenuType.MAIN_MENU
    #     self.selected_action_index=0
    #     self.menu_action = list(MenuAction)
    #     self.load_slots = list(saveSlot(),saveSlot(),saveSlot())
    #     self.menu_stack =[]
    #
    # def change_menu(self,menu_type:MenuType):
    #     self.menu_stack.append((self.current_menu,self.selected_action_index))
    #     self.current_menu = menu_type
    #     self.selected_action_index = 0
    #
    # def go_back(self):
    #     if self.menu_stack:
    #         self.current_menu,self.selected_action_index =self.menu_stack.pop()






    # def leave_game():
    #     sys.exit()







def display_confirmation_message():
    return texts.get(TextKey.GAME_CONFIRMATION_MESSAGE)


def confirmation_message()->bool:
    return True
    return False
if __name__ == "__main__":
    print(display_confirmation_message())