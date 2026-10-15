from dungeon.generator.maze_generation import Cell,CellType

def remaining_cell_type(dungeon: list[list[Cell]],cell_type:CellType):
    return [(i, j) for i, row in enumerate(dungeon) for j, cell in enumerate(row) if cell.type == cell_type]

