class Move:
    """
    Class move.

    :param type: type of move either normal or box_move
    :type type: string

    :param direction: type of move either normal or box_move
    :type direction: string

    :param player_was_at: where player is before the move
    :type player_was_at: two int tuple

    :param player_moves_to: where player should be moved
    :type player_moves_to: two int tuple

    :param box_moves_to: where box should be moved
    :type box_moves_to: two int tuple
    """

    def __init__(self, type, direction, player_was_at, player_to, box_to=None):
        """
        Creates instance of move
        """
        if type not in ("normal, box_move"):
            raise ValueError("Wrong move type")
        else:
            self._type = type

        if direction not in ("Up", "Down", "Right", "Left"):
            raise ValueError("Wrong move direction")
        else:
            self._direction = direction

        if not isinstance(player_was_at, tuple):
            raise TypeError("player_to has to be 2 int tuple")
        if len(player_was_at) != 2:
            raise TypeError("player_to has to be 2 int tuple")
        if not isinstance(player_was_at[0], int) or not isinstance(player_was_at[1], int):
            raise TypeError("player_to has to be 2 int tuple")
        self._player_was_at = player_was_at

        if not isinstance(player_to, tuple):
            raise TypeError("player_to has to be 2 int tuple")
        if len(player_to) != 2:
            raise TypeError("player_to has to be 2 int tuple")
        if not isinstance(player_to[0], int) or not isinstance(player_to[1], int):
            raise TypeError("player_to has to be 2 int tuple")
        self._player_moves_to = player_to

        if self.type() == "box_move":
            if not isinstance(box_to, tuple):
                raise TypeError("box_to has to be 2 int tuple")
            if len(box_to) != 2:
                raise TypeError("box_to has to be 2 int tuple")
            if not isinstance(box_to[0], int) or not isinstance(box_to[1], int):
                raise TypeError("box_to has to be 2 int tuple")
            self._box_moves_to = box_to

    def type(self):
        return self._type

    def player_moves_to(self):
        return self._player_moves_to

    def box_moves_to(self):
        return self._box_moves_to

    def direction(self):
        return self._direction

    def player_was_at(self):
        return self._player_was_at
