from dataclasses import dataclass

from dungeon.models.Point import Point


@dataclass
class Player:
    position: Point
    glyph: str = "@"

    def _set_position(self, position: Point):
        self.position = position
