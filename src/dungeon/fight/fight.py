from dungeon.generator.dungeon_elements.entities import  Character, Living
import dungeon.generator.dungeon_elements.monster_set as monsters
from enum import Enum,auto
def fight(character:Living,monster:Living):

    attacker,defender = (character,monster) if character.speed >=monster.speed else (monster,character)

    while True:
        attacker.health -= defender.skills
        print(attacker.name,"\t\tmade",attacker.atk,"dmg :\t",defender.name,"\t\t\t\thealth",defender.health)
        if attacker.health <=0:
           return defender
        print(defender.name,"made",defender.atk,"dmg :\t",attacker.name,"\t\t\t\thealth",attacker.health)
        defender.health -= attacker.atk
        if defender.health <=0:
           return attacker



class Action(Enum):
    OBJECT=auto()
    SKILL = auto()
    SIMPLE_ATTACK = auto()
    FLEE = auto()

def select_action():
    
    return




if __name__ == "__main__":
    hero = Character("Geralt",level=15, health=100, speed=12, atk=20)
    winner = fight(hero, monsters.SKELETTON)
    # Affichage du gagnant
    print(f"Le combat est terminé ! Le vainqueur est : {winner.name}")