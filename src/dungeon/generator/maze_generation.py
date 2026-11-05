from dungeon.models import Cell, CellType
import random

from dungeon.models import Direction, Point


Dungeon = list[list[Cell]]


def size_of(dungeon: Dungeon) -> tuple[int, int]:
    return len(dungeon[0]), len(dungeon)


def cell_at(dungeon: Dungeon, point: Point) -> Cell:
    return dungeon[point.y][point.x]


def set_cell(dungeon: Dungeon, point: Point, cell: Cell) -> None:
    dungeon[point.y][point.x] = cell


def in_bounds(dungeon: Dungeon, point: Point) -> bool:
    width, height = size_of(dungeon)
    return 0 <= point.x < width and 0 <= point.y < height


def is_inner(dungeon: Dungeon, point: Point) -> bool:
    width, height = size_of(dungeon)
    return 1 <= point.x < width - 1 and 1 <= point.y < height - 1


def expand_maze(width: int, height: int, depart: Point) -> Dungeon:
    dungeon = [[Cell(CellType.WALL) for _ in range(width)] for _ in range(height)]

    directions = list(Direction)
    pile = [depart]

    while pile:
        current = pile[-1]
        random.shuffle(directions)

        found = False
        for direction in directions:
            voisin = current.translate(direction, 2)

            if is_inner(dungeon, voisin) and cell_at(dungeon, voisin).type == CellType.WALL:
                set_cell(dungeon, current.translate(direction), Cell(CellType.ROOM))
                set_cell(dungeon, voisin, Cell(CellType.ROOM))

                pile.append(voisin)
                found = True
                break

        if not found:
            pile.pop()

    set_cell(dungeon, depart, Cell(CellType.STAIR_UP))
    dungeon = change_room_to(CellType.STAIR_DOWN, dungeon)
    return dungeon


def remaining_rooms(dungeon: Dungeon) -> list[Point]:
    return [Point(x, y)
            for y, row in enumerate(dungeon)
            for x, cell in enumerate(row)
            if cell.type == CellType.ROOM]


def remaining_dead_end(dungeon: Dungeon, rooms: list[Point]) -> list[Point]:
    treasure_compatible = []
    for room in rooms:
        voisins = [room.translate(direction) for direction in Direction]
        walls = sum(1 for voisin in voisins
                    if in_bounds(dungeon, voisin) and cell_at(dungeon, voisin).type == CellType.WALL)
        if walls == 3:
            treasure_compatible.append(room)
    return treasure_compatible


def change_room_to(cell_type: CellType, dungeon: Dungeon):
    rooms = remaining_rooms(dungeon)
    if not rooms:
        return None

    if cell_type == CellType.TREASURE:
        rooms = remaining_dead_end(dungeon, rooms)
        if not rooms:
            return None

    set_cell(dungeon, random.choice(rooms), Cell(cell_type))
    return dungeon


def add_element(dungeon: Dungeon, number_of_element: int, element_type: CellType):
    for _ in range(number_of_element):
        change_room_to(element_type, dungeon)
    return dungeon


def create_dungeon(level_design: tuple[int, int, int]):
    size, monster, treasure = level_design

    depart = Point(random.randrange(1, size - 1, 2), random.randrange(1, size - 1, 2))

    dungeon = expand_maze(size, size, depart)
    if not dungeon:
        return None
    dungeon = add_element(dungeon, monster, CellType.MONSTER)
    return add_element(dungeon, treasure, CellType.TREASURE)
