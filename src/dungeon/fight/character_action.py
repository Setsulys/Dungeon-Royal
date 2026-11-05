from enum import Enum,auto
from dungeon.common_tools.input_handler import Input

selected_action_index=0

class Action(Enum):
    SIMPLE_ATTACK = auto()
    SKILL = auto()
    OBJECT = auto()
    FLEE = auto()



def select_action(selector):
    global selected_action_index
    nb_action=len(Action)
    if selector ==Input.UP:
        selected_action_index = (selected_action_index -1)% nb_action
    elif selector ==Input.DOWN:
        selected_action_index = (selected_action_index +1)% nb_action
    elif selector == Input.CONFIRM:
        return Action(selected_action_index)
    elif selector == Input.CANCEL:
        return Action.FLEE
    return None
