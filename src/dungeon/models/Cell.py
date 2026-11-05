from dungeon.models.CellType import CellType

class Cell:
    def __init__(self, cell_type: CellType, entity=None):
        self.type = cell_type
        self.entity = entity