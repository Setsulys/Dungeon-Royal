from dataclasses import dataclass


@dataclass(frozen=True)
class Point:
    x: int
    y: int

    def distance_manhattan(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    def adding(self, dx: int, dy: int) -> 'Point':
        return Point(self.x + dx, self.y + dy)

    def translate(self, direction, times: int = 1) -> 'Point':
        return self.adding(direction.dx * times, direction.dy * times)
