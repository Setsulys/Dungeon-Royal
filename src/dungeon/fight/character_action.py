from enum import Enum,auto

from pip import __main__

from dungeon.common_tools.input_handler import Input
from dungeon.generator.dungeon_elements.entities import Character,Skill,Item

class Action(Enum):
    SIMPLE_ATTACK = auto()
    SKILL = auto()
    OBJECT = auto()
    FLEE = auto()


class MenuType(Enum):
    MAIN_BATTLE_MENU = auto()
    SKILL_MENU = auto()
    ITEM_MENU = auto()

class BattleMenu:
    def __init__(self,character:Character):
        self.skills = character.skills
        self.items = character.items

        self.selected_action_index=0
        self.current_menu = MenuType.MAIN_BATTLE_MENU
        self.menu_action = list(Action)
        self.menu_stack=[]

    def change_menu(self,menu_type:MenuType):
        self.menu_stack.append((self.current_menu,self.selected_action_index))
        self.current_menu = menu_type
        self.selected_action_index = 0


    def go_back(self):
        if self.menu_stack:
            self.current_menu,self.selected_action_index = self.menu_stack.pop()

    def battle_menu_handler(self,selector):
        match self.current_menu:
            case MenuType.MAIN_BATTLE_MENU:
                elements = self.menu_action
            case MenuType.ITEM_MENU:
                elements = self.items
            case MenuType.SKILL_MENU:
                elements = self.skills
        if not elements:
            return None
        nb_elements = len(elements)

        match selector:
            case Input.UP:
                self.selected_action_index = (self.selected_action_index -1)% nb_elements
            case Input.DOWN:
                self.selected_action_index = (self.selected_action_index +1)% nb_elements
            case Input.CONFIRM:
                return elements[self.selected_action_index]
            case Input.CANCEL:
                if self.current_menu==MenuType.MAIN_BATTLE_MENU:
                    return Action.FLEE
                else:
                    self.go_back()
        return None

    def main_battle_menu(self,selector):
        selection = self.battle_menu_handler(selector)
        match selection:
            case Action.SIMPLE_ATTACK:
                return "ATTACK"
            case Action.SKILL:
                if self.skills:
                    self.change_menu(MenuType.SKILL_MENU)
                return None
            case Action.OBJECT:
                if self.items:
                    self.change_menu(MenuType.ITEM_MENU)
                return None
            case _:
                return selection




    def display_menu(self):
        match self.current_menu:
            case MenuType.MAIN_BATTLE_MENU:
                elements = self.menu_action
            case MenuType.SKILL_MENU:
                elements = self.skills
            case MenuType.ITEM_MENU:
                elements = self.items

        print(f"\n--- {self.current_menu.name} ---")

        for i, element in enumerate(elements):
            cursor = ">" if i == self.selected_action_index else " "
            print(f"{cursor} {element}")


if __name__ == "__main__":
    character = Character("Darkness", 10, 100, 2, 100)

    slash = Skill("Slash",100)
    decoy = Skill("Decoy",1)

    heal = Item("healing potion")
    expl = Item("Explosion potion")

    character.learn_skill(slash,1)
    character.learn_skill(decoy,100)

    character.get_items(heal,heal,heal,expl,heal)
    menu = BattleMenu(character)

    while True:
        menu.display_menu()

        key = input(
            "\n[z] Haut | [s] Bas | [ ] Confirmer "
            "| [q] Retour | [x] Quitter : "
        ).lower()

        if key == "x":
            break
        elif key == "z":
            selector = Input.UP
        elif key == "s":
            selector = Input.DOWN
        elif key == "q":
            selector = Input.CANCEL
        elif key == "":
            selector = Input.CONFIRM
        else:
            continue

        result = menu.main_battle_menu(selector)

        if result is not None:
            print(f"\nAction retournée : {result}")
            input("Appuie sur Entrée pour continuer...")

