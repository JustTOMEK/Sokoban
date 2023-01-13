from tile import Wall, Box, Player, Floor
from move import BoxMove, NormalMove


class Map:
    """
    Class map.
    Input map_str, that is str created by file.read().
    Contains attributes:

    :param tiles: current state of a map
    :type tiles: list of lists of tiles

    :param targets: targets of map
    :type targets: list of lists

    :param move_count: number of moves made
    :type move_count: int

    :param rows: number of rows
    :type rows: int

    :param columns: number of columns
    :type columns: int

    :param moves: list of moves made so far
    :type moves: list of move objects
    """
    def __init__(self, map_str):
        self._tiles = self.str_map_to_tiles(map_str.replace(" ", ""))
        self._rows = len(self.tiles())
        self._columns = len(self.tiles()[0])
        self._targets = self.target_coordinates()
        self._moves = []
        self._move_count = 0

    def str_map_to_tiles(self, map_in_str):
        """
        Method reads string and creates tile map out of it
        """
        tile_map = [[]]
        row_number = 0
        char_to_instance = {'f': Floor, 'p': Player, 'w': Wall, 'b': Box}
        for char in map_in_str:
            if char == "\n":
                row_number += 1
                tile_map.append([])
            else:
                new_tile = char_to_instance[char.lower()](char.isupper())
                tile_map[row_number].append(new_tile)
        # checking if map is a rectangle
        lengths_of_rows = set()
        for row in tile_map:
            lengths_of_rows.add(len(row))
        if len(lengths_of_rows) != 1:
            raise ValueError("Map has to be rectangle")
        return tile_map

    def move_count(self):
        return self._move_count

    def moves(self):
        return self._moves

    def tiles(self):
        return self._tiles

    def columns(self):
        return self._columns

    def rows(self):
        return self._rows

    def targets(self):
        return self._targets

    def add_move(self, move):
        """
        Method adds move
        """
        if isinstance(move, BoxMove) or isinstance(move, NormalMove):
            self._moves.append(move)
            self._move_count += 1
        else:
            raise ValueError("You can only add move objects to move list.")

    def delete_last_move(self):
        self._move_count -= 1
        return self._moves.pop()

    def player_position(self):
        """
        Method returns player coordinates in tuple
        """
        for row_number, row in enumerate(self.tiles()):
            for column_number, tile in enumerate(row):
                if isinstance(tile, Player):
                    return (row_number, column_number)

    def target_coordinates(self):
        """
        Method target_coordinates, check where are targets
        Returns list of coordinates  that are targets
        list is sorted by row, the column
        [(0,1), (0,2), (3,0)]
        """
        targets = []
        for row_number, row in enumerate(self.tiles()):
            for column_number, tile in enumerate(row):
                if tile.is_target():
                    targets.append((row_number, column_number))
        return targets

    def available_moves(self):
        """
        Method available_moves, check what moves can player name
        Returns list of coordinates player can go to and direction
        [[0,1], 'R', [0,2], 'L', [3,0], 'U']
        Checks in order up, right, down, left
        """
        player_row, player_column = self.player_position()
        moves = []
        # directions list contains what coordinate player moves and box moves
        directions = [['Up', [-1, 0], [-2, 0]], ['Right', [0, 1], [0, 2]],
                      ['Down', [1, 0], [2, 0]], ['Left', [0, -1], [0, -2]]]
        # not checking if player can move up if is in first row
        # the same case for last row down and columns
        if player_row == 0:
            del directions[0]
        if player_row == self.rows() - 1:
            del directions[2]
        if player_column == 0:
            del directions[3]
        if player_column == self.columns() - 1:
            del directions[1]
        for direction in directions:
            # creating variables that hold tiles one and two away
            # in given direction
            direction, one_away, two_away = direction
            one_away_row = player_row + one_away[0]
            one_away_column = player_column + one_away[1]
            tile_one_away = self.tiles()[one_away_row][one_away_column]
            two_away_row = player_row + two_away[0]
            two_away_column = player_column + two_away[1]
            # if a tile two away is out of map range, it changes to a wall
            # so player won't be able to make into it
            if (two_away_row not in range(0, self.rows()) or
               two_away_column not in range(0, self.columns())):
                tile_two_away = Wall(False)
            else:
                tile_two_away = self.tiles()[two_away_row][two_away_column]
            # checking if normal move, or box_move are available
            if tile_one_away.can_move_into():
                if isinstance(tile_one_away, Floor):
                    moves.append(NormalMove(direction,
                                            (player_row, player_column),
                                            (one_away_row, one_away_column)))

                elif (isinstance(tile_one_away, Box)
                      and isinstance(tile_two_away, Floor)):
                    moves.append(BoxMove(direction,
                                         (player_row, player_column),
                                         (one_away_row, one_away_column),
                                         (two_away_row, two_away_column)))
        return moves

    def move(self, direction):
        """
        Method moves player in given direction if move is legal.
        If move involves moving box, it will also move box.
        Takes direction Up, Right, Down, Left
        If move is in available_moves returns True and makes the move
        If not returns False
        """
        if direction not in ["Up", "Right", "Left", "Down"]:
            raise ValueError("Wrong Direction")
        for move in self.available_moves():
            if move.direction() == direction:
                player_x, player_y = move.player_was_at()
                player_to_x, player_to_y = move.player_moves_to()
                if isinstance(move, BoxMove):
                    box_to_row, box_to_column = move.box_moves_to()
                    self.swap_tiles((player_to_x, player_to_y),
                                    (box_to_row, box_to_column))
                    self.swap_tiles((player_x, player_y),
                                    (player_to_x, player_to_y))
                elif isinstance(move, NormalMove):
                    self.swap_tiles((player_x, player_y),
                                    (player_to_x, player_to_y))
                self.add_move(move)
                return True
        return False

    def check_if_win(self):
        """
        Method checks if game on current map has ended.
        For map to end every target coordinate tile has to be a box
        """
        for row, column in self.targets():
            if not isinstance(self.tiles()[row][column], Box):
                return False
        return True

    def undo_move(self):
        """
        Method undos last made move.
        It takes last made move from move list
        Then it reverses things done in move
        """
        if self._move_count == 0:
            return None
        move = self.delete_last_move()
        player_row, player_column = move.player_was_at()
        player_to_row, player_to_column = move.player_moves_to()
        if isinstance(move, BoxMove):
            box_to_row, box_to_column = move.box_moves_to()
            self.swap_tiles((player_to_row, player_to_column),
                            (box_to_row, box_to_column))
            self.swap_tiles((player_row, player_column),
                            (box_to_row, box_to_column))
        elif isinstance(move, NormalMove):
            self.swap_tiles((player_row, player_column),
                            (player_to_row, player_to_column))
        return True

    def swap_tiles(self, tile_1_coords, tile_2_coords):
        """
        Method swaps two tiles on given coordinates
        Coordinates should be two int touples
        If tile on given coordinates was a target
        Then it changes new tile on given coordinates to a targets
        """
        # checks if coordinates in map range
        if (tile_1_coords[0] > self.rows() - 1 or
           tile_2_coords[0] > self.rows() - 1 or
           tile_1_coords[1] > self.columns() - 1 or
           tile_2_coords[1] > self.columns() - 1):
            raise ValueError("Coordinates out of map range")
        # unpacks coordinate data
        x_1 = tile_1_coords[0]
        y_1 = tile_1_coords[1]
        x_2 = tile_2_coords[0]
        y_2 = tile_2_coords[1]
        tile_1_is_target = self._tiles[x_1][y_1].is_target()
        tile_2_is_target = self._tiles[x_2][y_2].is_target()
        # swaps tiles
        self._tiles[x_1][y_1], self._tiles[x_2][y_2], = (self._tiles[x_2][y_2],
                                                         self._tiles[x_1][y_1])
        self._tiles[x_1][y_1].set_is_target(tile_1_is_target)
        self._tiles[x_2][y_2].set_is_target(tile_2_is_target)
