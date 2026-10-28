from dungeon.models import Direction
from dungeon.models.Cell import Cell
from dungeon.models.CellType import CellType
from dungeon.models.Point import Point

class Grid:
    _cells: dict[Point, Cell]
    _height: int
    _width: int

    def __init__(self, width: int, height: int, cells: dict[Point, Cell]):
        if len(cells) != width * height:
            raise ValueError(f"grille incomplete : {len(cells)} cases pour {width}x{height}")

        self._width = width
        self._height = height
        self._cells = cells


    @classmethod
    def filled(cls, width: int, height: int, cell_type: CellType) -> "Grid":
        cells = {}

        for y in range(height):
            for x in range(width):
                point = Point(x, y)
                cell = Cell(cell_type)
                cells[point] = cell

        return cls(width, height, cells)


    @property
    def width(self) -> int:
        return self._width

    @property
    def height(self) -> int:
        return self._height

    def __getitem__(self, point: Point) -> Cell:
        return self._cells[point]

    def __setitem__(self, point: Point, cell: Cell) -> None:
        if point not in self._cells:
            raise KeyError(f"{point} est hors de la grille {self.width}x{self.height}")
        self._cells[point] = cell

    def __contains__(self, point: Point) -> bool:
        return point in self._cells

    def __iter__(self):
        return iter(self._cells)

    def is_inner(self, point: Point) -> bool:
        return 1 <= point.x < self.width - 1 and 1 <= point.y < self.height - 1

    def is_crossable(self, point: Point) -> bool:
        return point in self._cells and self[point].type.is_crossable

    def neighbors(self, point: Point, step: int = 1) -> list[Point]:
        voisins = (point.translate(direction, step) for direction in Direction)
        return [voisin for voisin in voisins if voisin in self._cells]