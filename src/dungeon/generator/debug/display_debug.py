from dungeon.generator.maze_generation import create_dungeon
from dungeon.generator.leveldesign import compute_element_from_character_level
from dungeon.models import Grid, Point
from dungeon.models.CellType import CellType

symbols = {
    CellType.WALL: "■",
    CellType.ROOM: " ",
    CellType.MONSTER: "0",
    CellType.TREASURE: "T",
    CellType.STAIR_UP: "U",
    CellType.STAIR_DOWN: "D"
}

def display_dungeon(grid: Grid) -> None:
    for y in range(grid.height):
        print(" ".join(symbols[grid[Point(x, y)].type] for x in range(grid.width)))

def display_maze(level):
    dungeon =  create_dungeon(compute_element_from_character_level(level))
    if not dungeon:
        return
    display_dungeon(dungeon)
