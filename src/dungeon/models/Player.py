from dataclasses import dataclass

@dataclass
class Player:
    position: Point
    glyph: str = "@"

    def move_to(self, position: Point):
        self.position = position