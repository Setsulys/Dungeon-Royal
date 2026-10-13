class Monster:
    def __init__(self, name, health,atk):
        self.name = name
        self.health = health
        self.atk = atk

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

monster = Monster("Gobelin", 20,100)
treasure = Treasure("Pièces d'or", 100)