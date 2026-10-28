from dungeon.models import Cell, CellType, Grid
import random

from dungeon.models import Direction, Point


def expand_maze(width: int, height: int, depart: Point) -> Grid:
    if width < 5 or height < 5 or width % 2 == 0 or height % 2 == 0:
        raise ValueError(f"dimensions invalides : {width}x{height} "
                         f"(attendu : impaires et >= 5)")
    grid = Grid.filled(width, height, CellType.WALL)

    directions = list(Direction)
    pile = [depart]

    while pile:
        current = pile[-1]
        random.shuffle(directions)

        found = False
        for direction in directions:
            voisin = current.translate(direction, 2)

            if grid.is_inner(voisin) and grid[voisin].type == CellType.WALL:
                grid[current.translate(direction)] = Cell(CellType.ROOM)
                grid[voisin] = Cell(CellType.ROOM)

                pile.append(voisin)
                found = True
                break

        if not found:
            pile.pop()

    grid[depart] = Cell(CellType.STAIR_UP)
    rooms = remaining_rooms(grid)
    grid[max(rooms, key=depart.distance_manhattan)] = Cell(CellType.STAIR_DOWN)
    return grid


def remaining_rooms(grid: Grid) -> list[Point]:
    return [point for point in grid if grid[point].type == CellType.ROOM]


def remaining_dead_end(grid: Grid, rooms: list[Point]) -> list[Point]:
    treasure_compatible = []
    for room in rooms:
        voisins = [room.translate(direction) for direction in Direction]
        walls = sum(1 for voisin in voisins
                    if voisin in grid and grid[voisin].type == CellType.WALL)
        if walls == 3:
            treasure_compatible.append(room)
    return treasure_compatible


def change_room_to(cell_type: CellType, grid: Grid):
    rooms = remaining_rooms(grid)
    if not rooms:
        return None

    if cell_type == CellType.TREASURE:
        rooms = remaining_dead_end(grid, rooms)
        if not rooms:
            return None

    grid[random.choice(rooms)] = Cell(cell_type)
    return grid


def add_element(grid: Grid, number_of_element: int, element_type: CellType):
    for _ in range(number_of_element):
        change_room_to(element_type, grid)
    return grid


def create_dungeon(level_design: tuple[int, int, int]):
    size, monster, treasure = level_design

    depart = Point(random.randrange(1, size - 1, 2), random.randrange(1, size - 1, 2))

    grid = expand_maze(size, size, depart)

    dungeon = add_element(grid, monster, CellType.MONSTER)
    return add_element(dungeon, treasure, CellType.TREASURE)