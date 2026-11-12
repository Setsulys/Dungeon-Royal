from enum import Enum, auto


class CellType(Enum):
    WALL = auto()
    ROOM = auto()
    MONSTER = auto()
    TREASURE = auto()
    STAIR_UP = auto()
    STAIR_DOWN = auto()

    @property
    def is_crossable(self) -> bool:
        return self not in _NON_CROSSABLE


_NON_CROSSABLE = frozenset({CellType.WALL})
