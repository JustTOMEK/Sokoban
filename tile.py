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

    def set_is_target(self, is_target):
        if not isinstance(is_target, bool):
            raise ValueError("is_target has to be a bool")
        self._is_target = is_target


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
    def __init__(self, is_target):
        if is_target:
            raise ValueError("Wall cannot be a target")
        super().__init__(is_target)

    def can_move_into(self):
        return False

    def set_is_target(self, is_target):
        if is_target:
            raise ValueError("Wall cannot be a target")
        self._is_target = is_target


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
