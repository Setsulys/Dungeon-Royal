from enum import Enum

from dungeon.models.Point import Point


class Direction(Enum):
    UP = Point(0, -1)
    DOWN = Point(0, 1)
    LEFT = Point(-1, 0)
    RIGHT = Point(1, 0)

    @property
    def dx(self):
        return self.value.x

    @property
    def dy(self):
        return self.value.y

