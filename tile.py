from abc import ABC


class Tile(ABC):
    """
    Class tile.
    """
    def __init__(self, is_target):
        if not isinstance(is_target, bool):
            raise ValueError("is_target has to be a bool")
        self._is_target = is_target

    def can_move_into(self):
        return False

    def is_target(self):
        return self._is_target


class Floor(Tile):
    """
    Class Floor
    """
    def can_move_into(self):
        return True


class Wall(Tile):
    """
    Class Wall.
    """
    def can_move_into(self):
        return False


class Player(Tile):
    """
    Player tile.
    """
    def can_move_into(self):
        return False


class Box(Tile):
    """
    Box tile.
    """
    def can_move_into(self):
        return True
