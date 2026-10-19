

class TileType(Enum):
    WALL = ("#", False)
    GROUND = (".", True)
    STAIRS = ("E", True)

    def __init__(self, glyphe: str, is_crossable: bool):
        self.glyphe = glyphe
        self.is_crossable = is_crossable
