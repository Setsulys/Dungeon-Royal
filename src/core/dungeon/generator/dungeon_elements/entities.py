import random

class StatusEffect:
    def __init__(self, name: str, duration: int, dmg_per_turn: int = 0, speed_modifier: int = 0):
        self.name = name
        self.duration = duration  # Nombre de tours restants
        self.dmg_per_turn = dmg_per_turn
        self.speed_modifier = speed_modifier
class Skill:
    def __init__(self, name: str, damage: int, effect: StatusEffect = None):
        self.name = name
        self.damage = damage
        self.effect = effect

    def __str__(self) -> str: return f"{self.name}: {self.damage} dmg"

class Item:
    def __init__(self, name: str):
        self.name = name

    def __str__(self) -> str: return f"{self.name}"

class Living:
    def __init__(self, name: str,level:int, health:int,speed:int,atk:int):
        self.name = name
        self.level = level
        self.health = health
        self.base_speed = speed
        self.speed = speed
        self.atk = atk
        self.skills = []
        self.items=[]
        self.precision = []
        self.status_effect=[]

    def learn_skill(self,skill:Skill,precision:int):
        self.skills.append(skill)
        self.precision.append(precision)

    def get_items(self,*item:Item):
        for e in item:
            self.items.append(e)

    def use_item(self,item:Item):
        self.items.remove(item)


class Character(Living):
    pass

class Monster(Living):
    def __init__(self, name: str, level: int, health: int, speed: int, atk: int):
        super().__init__(name, level, health, speed, atk)
        self.skills_chance = {}

    def learn_monster_skill(self, skill: Skill, chance: int):
        self.skills.append(skill)
        self.skills_chance[skill] = chance

    def choose_action(self)->Skill:
        weights = [self.skills_chance.get(s, 1) for s in self.skills]
        chosen_skill = random.choices(self.skills, weights=weights, k=1)
        return chosen_skill[0]
