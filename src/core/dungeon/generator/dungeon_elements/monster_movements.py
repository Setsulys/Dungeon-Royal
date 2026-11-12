import random

from dungeon.models import CellType, Grid, Point, Cell


def all_monster_movements(grid: Grid) -> None:
    for position in grid.points_of_type(CellType.MONSTER):
        monster_movement(grid, position)

def monster_movement(grid: Grid, position: Point) -> None:
    cibles = [p for p in grid.neighbors(position) if grid[p].type in (CellType.ROOM, CellType.MONSTER)]
    cibles.append(position)

    cible = random.choice(cibles)

    if cible == position:
        return

    grid[cible] = Cell(CellType.MONSTER)
    grid[position] = Cell(CellType.ROOM)