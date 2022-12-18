from enum import Enum


class ShapeType(Enum):
    I_Shape = 1
    O_Shape = 2
    T_Shape = 3
    S_Shape = 4
    Z_Shape = 5
    J_Shape = 6
    L_Shape = 7


class Shape:

    def __init__(self):
        self.OccupiedTiles = []
        self.ShapeType = None
