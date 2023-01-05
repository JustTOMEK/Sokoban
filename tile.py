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
        char_to_full = {"f": "floor",
                        "w": "wall",
                        "p": "player",
                        "b": "box"}
        if char_type not in char_to_full:
            raise TypeError("Wrong tile char")
        return char_to_full[char_type]

    def is_target(self):
        return self._is_target

    def set_type(self, new_type):
        if not isinstance(new_type, str):
            raise TypeError("type has to be a char")
        if len(new_type) != 1:
            raise TypeError("type has to be a char")
        if new_type == "W":
            raise ValueError("wall can not be a target")
        self._type = self.full_type(new_type.lower())
        self._is_target = new_type.isupper()

    def type(self):
        return self._type
