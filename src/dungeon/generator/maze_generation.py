from enum import Enum,auto
from dungeon.common_tools.common_tools import remaining_cell_type
import random


class CellType(Enum):
    WALL = auto()
    ROOM = auto()
    MONSTER = auto()
    TREASURE = auto()
    STAIR_UP = auto()
    STAIR_DOWN = auto()

class Cell:
    def __init__(self, cell_type, entity=None):
        self.type = cell_type
        self.entity = entity


def expand_maze(maze_size:tuple[int,int],depart:tuple[int,int]):
    maze_height,maze_width=maze_size
    dx,dy=depart
    dungeon = [[Cell(CellType.WALL) for _ in range(maze_width)] for _ in range(maze_height)]

    directions = [(-2,0),(2,0),(0,-2),(0,2)]

    pile = [depart]

    while pile:
        row,column=pile[-1]
        random.shuffle(directions)

        found = False
        for dl,dc in directions:
            nl = row+dl
            nc = column+dc

            if (1 <= nl < maze_height - 1
                    and 1 <= nc < maze_width - 1
                    and dungeon[nl][nc].type == CellType.WALL):

                dungeon[row + dl // 2][column + dc // 2] = Cell(CellType.ROOM)

                dungeon[nl][nc] = Cell(CellType.ROOM)

                pile.append((nl, nc))
                found = True
                break

        if not found:
            pile.pop()
    dungeon[dx][dy].type=CellType.STAIR_UP
    dungeon = change_room_to(CellType.STAIR_DOWN,dungeon)
    return dungeon



def remaining_dead_end(dungeon: list[list[Cell]],rooms:list[tuple[int,int]]):
    treasure_compatible = []
    for x,y in rooms:
        walls =sum(1 for i,j in ((x - 1, y),(x + 1, y),(x, y - 1),(x, y + 1)) if 0 <= i < len(dungeon) and 0 <= j < len(dungeon[i]) and dungeon[i][j].type == CellType.WALL)
        if walls == 3:
            treasure_compatible.append((x, y))
    return treasure_compatible

def change_room_to(cell_type:CellType,dungeon: list[list[Cell]]):
    rooms = remaining_cell_type(dungeon,CellType.ROOM)
    if not rooms:
        return None

    if cell_type == CellType.TREASURE:
        rooms = remaining_dead_end(dungeon,rooms)
        if not rooms:
            return None
    x,y = random.choice(rooms)

    dungeon[x][y] = Cell(cell_type)
    return dungeon


def add_element(dungeon: list[list[Cell]],number_of_element:int,element_type:CellType):
    for _ in range(number_of_element):
        change_room_to(element_type,dungeon)
    return dungeon

def create_dungeon(level_design:tuple[int,int,int]):

    size,monster,treasure = level_design
    maze_size = (size,size)

    #randomize depart position
    depart_position = (random.randrange(1,size-1,2),random.randrange(1,size-1,2))

    # create maze and add stairs
    dungeon = expand_maze(maze_size,depart_position)
    # Add the entities to the dungeon
    if not dungeon:
        return None
    dungeon =add_element(dungeon,monster,CellType.MONSTER)
    return add_element(dungeon,treasure,CellType.TREASURE)


