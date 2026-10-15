import random

from dungeon.generator.maze_generation import Cell,CellType
from dungeon.generator.common_tools.common_tools import remaining_cell_type


def all_monster_movements(dungeon:list[list[Cell]]):
    monster_positions =remaining_cell_type(dungeon,CellType.MONSTER)
    dungeon =list(map(lambda x: monster_movement(dungeon,*x[1:]),monster_positions))
    return dungeon

def monster_movement(dungeon:list[list[Cell]],x:int,y:int):
    movements=[(-1, 0), (1, 0), (0, -1), (0, 1),(0,0)]
    possible_movements=[
        (nx, ny)
        for dx, dy in movements
        if dungeon[nx := x + dx][ny := y + dy].type in (CellType.ROOM,CellType.MONSTER)
    ]

    # si le monstre ne bouge pas on change rien
    i,j = random.choice(possible_movements)
    if i==x and j==y:
        return dungeon
    # si le monstre bouge, on inverse avec room
    dungeon[i][j].type=CellType.MONSTER
    dungeon[x][y].type=CellType.ROOM

    return dungeon