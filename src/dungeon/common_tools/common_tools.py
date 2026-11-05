from dungeon.models import Cell, CellType, Point, Grid


def remaining_cell_type(grid: Grid, cell_type: CellType) -> list[Point]:
    return [point for point in grid if grid[point].type == cell_type]