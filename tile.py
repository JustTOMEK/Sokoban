class Tile:
    """
    Class tile.

    :param type: type of a tile
    :type type: string

    :param is_target: if tile is a target
    :type is_target: bool
    """
    def __init__(self, char_type):
        """
        Initializes tile instance
        """
        if not isinstance(char_type, str):
            raise TypeError("char_type has to be a char")
        if len(char_type) != 1:
            raise TypeError("char_type has to be a char")
        if char_type == "W":
            raise ValueError("wall can not be a target")
        self._is_target = char_type.isupper()
        self._type = self.full_type(char_type.lower())

    def full_type(self, char_type):
        """
        Translates char to full tyoe name.
        """
        char_to_full = {"f": "floor",
                        "w": "wall",
                        "p": "player",
                        "b": "box"}
        if char_type not in char_to_full:
            raise TypeError("Wrong tile char")
        return char_to_full[char_type]

    def set_type(self, new_type):
        if new_type not in ["wall", "floor", "player", "box"]:
            raise ValueError("Wrong new_type")
        self._type = new_type

    def type(self):
        return self._type

    def is_target(self):
        return self._is_target


def swap_tiles(tile_1, tile_2):
    """
    Swaps to tiles.
    is_target stays the same and type changes.
    """
    if not isinstance(tile_1, Tile) or not isinstance(tile_2, Tile):
        raise TypeError("tiles have to be tile objects")
    if tile_1.type() == "wall" or tile_2.type() == "wall":
        raise ValueError("Walls cannot be swapped")
    tile_1_type = tile_1.type()
    tile_1.set_type(tile_2.type())
    tile_2.set_type(tile_1_type)
