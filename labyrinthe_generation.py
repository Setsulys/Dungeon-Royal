from enum import Enum,auto
import random

class CellType(Enum):
    WALL = auto()
    ROOM = auto()
    MONSTER = auto()
    TREASURE = auto()
    STAIR_UP = auto()
    STAIR_DOWN = auto()

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    RIGHT = auto()
    LEFT = auto()

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

class Cell:
    def __init__(self, cell_type, entity=None):
        self.type = cell_type
        self.entity = entity



symbols = {
    CellType.WALL: "■",
    CellType.ROOM: " ",
    CellType.MONSTER: "M",
    CellType.TREASURE: "T",
    CellType.STAIR_UP: "U",
    CellType.STAIR_DOWN: "D"
}

labyrinthe_height = 43
labyrinthe_width = 73
stair_up_positionx=25
stair_up_positiony=23



def expand_labyrinthe():
    dungeon = [[Cell(CellType.WALL) for _ in range(labyrinthe_width)] for _ in range(labyrinthe_height)]

    depart = (stair_up_positionx,stair_up_positiony)

    directions = [
        (-2,0),
        (2,0),
        (0,-2),
        (0,2),
    ]

    pile = [depart]

    while pile:
        ligne,colonne=pile[-1]
        random.shuffle(directions)

        trouve = False
        for dl,dc in directions:
            nl = ligne+dl
            nc = colonne+dc

            if (1 <= nl < labyrinthe_height - 1
                    and 1 <= nc < labyrinthe_width - 1
                    and dungeon[nl][nc].type == CellType.WALL):

                dungeon[ligne + dl // 2][colonne + dc // 2] = Cell(CellType.ROOM)

                dungeon[nl][nc] = Cell(CellType.ROOM)

                pile.append((nl, nc))
                trouve = True
                break

        if not trouve:
            pile.pop()

    return dungeon

def change_room_to(cell_type:CellType,dungeon: list[list[Cell]]):
    positions = [(i, j) for i, row in enumerate(dungeon) for j, cell in enumerate(row) if cell.type == CellType.ROOM]
    if not positions:
        return None
    random_room = random.choice(positions)
    x,y = random_room
    dungeon[x][y]=Cell(cell_type)
    return dungeon


def labyrinthe_add_both_stairs(dungeon: list[list[Cell]]):
    dungeon = change_room_to(CellType.STAIR_UP,dungeon)

    return change_room_to(CellType.STAIR_DOWN,dungeon)

def add_element(dungeon: list[list[Cell]],number_of_element:int,element_type:CellType):
    for _ in range(number_of_element):
        change_room_to(element_type,dungeon)
    return dungeon

def create_dungeon(nb_monster,nb_treasure):
    dungeon = expand_labyrinthe()
    dungeon = labyrinthe_add_both_stairs(dungeon)
    dungeon =add_element(dungeon,nb_monster,CellType.MONSTER)
    return add_element(dungeon,nb_treasure,CellType.TREASURE)
     

def character_is_in_wall(dungeon: list[list[Cell]],x,y):
    if dungeon[x][y].type == CellType.WALL:
        return 1
    return 0


def character_movement(dungeon,x,y,direction):
    match direction:
        case Direction.UP:
            return dungeon[x][y] == CellType.ROOM
        case Direction.DOWN:
            return dungeon[x][y] == CellType.ROOM
        case Direction.LEFT:
            return dungeon[x][y] == CellType.ROOM
        case Direction.RIGHT:
            return dungeon[x][y] == CellType.ROOM



def afficher_labyrinthe():
    dungeon =  create_dungeon(10,8)
    for row in dungeon:
        print(" ".join(symbols[cell.type] for cell in row))

afficher_labyrinthe()
