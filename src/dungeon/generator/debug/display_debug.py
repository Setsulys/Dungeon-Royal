from maze_generation import create_dungeon,CellType
from leveldesign import compute_element_from_character_level

symbols = {
    CellType.WALL: "■",
    CellType.ROOM: " ",
    CellType.MONSTER: "M",
    CellType.TREASURE: "T",
    CellType.STAIR_UP: "U",
    CellType.STAIR_DOWN: "D"
}

def display_dungeon(dungeon:list[list[CellType]]):
    for row in dungeon:
        print(" ".join(symbols[cell.type] for cell in row))
def display_maze(level):
    dungeon =  create_dungeon(compute_element_from_character_level(level))
    if not dungeon:
        return
    display_dungeon(dungeon)
