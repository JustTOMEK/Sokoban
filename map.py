from tile import Tile, swap_tiles
from move import Move


class Map:
    """
    Class map.
    Takes map_str, that is str created by file.read().
    Contains attributes:

    :param tiles: current state of a map
    :type tiles: list of lists of tiles

    :param targets: targets at start map
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
        tile_map = [[]]
        row_number = 0
        for char in map_in_str:
            if char == "\n":
                row_number += 1
                tile_map.append([])
            else:
                tile_map[row_number].append(Tile(char))
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

    def player_position(self):
        """
        :property player_position: position of a player
        :type player_position: two element list [row, column]
        """
        for row_number, row in enumerate(self.tiles()):
            for column_number, tile in enumerate(row):
                if tile.type() == "player":
                    return [row_number, column_number]

    def check_coordinates(self, coordinates):
        """
        takes data in two int touple (1, 2)
        Checks what is at given coordinates.
        Returns type of tile at coordinates
        """
        if not isinstance(coordinates, tuple):
            raise TypeError("coordinates has to be 2 int tuple")
        elif len(coordinates) != 2:
            raise TypeError("coordinates has to be 2 int tuple")
        row, column = coordinates
        if not isinstance(row, int) or not isinstance(column, int):
            raise TypeError("coordinates has to be 2 int tuple")
        if row not in range(0, self._rows) or column not in range(0, self._columns):
            return ValueError("row and column have to be in map range")
        return self.tiles()[row][column].type()

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
        for direction in directions:
            direction, player, box = direction
            condition_normal = self.check_coordinates((player_row + player[0], player_column + player[1])) == 'floor'
            condition__box_one = self.check_coordinates((player_row + player[0], player_column + player[1])) == 'box'
            condition_box_two = self.check_coordinates((player_row + box[0], player_column + box[1])) == 'floor'
            if condition_normal:
                moves.append(Move("normal", direction, (player_row, player_column), (player_row + player[0], player_column + player[1])))
            if condition__box_one and condition_box_two:
                moves.append(Move("box_move", direction, (player_row, player_column), (player_row + player[0], player_column + player[1]), (player_row + box[0], player_column + box[1])))
        return moves

    def move(self, direction):
        """
        Method moves player in given direction if move is legal.
        If move involves moving box, it will also move box.
        Takes direction Up, Right, Down, Left
        """
        if direction not in ["Up", "Right", "Left", "Down"]:
            raise ValueError("Wrong Direction")
        for move in self.available_moves():
            if move._direction == direction:
                player_row, player_column = move.player_was_at()
                player_to_row, player_to_column = move.player_moves_to()
                if move.type() == "normal":
                    swap_tiles(self.tiles()[player_row][player_column], self.tiles()[player_to_row][player_to_column])
                elif move.type() == "box_move":
                    box_to_row, box_to_column = move.box_moves_to()
                    swap_tiles(self.tiles()[player_to_row][player_to_column], self.tiles()[box_to_row][box_to_column])
                    swap_tiles(self.tiles()[player_row][player_column], self.tiles()[player_to_row][player_to_column])
                self._moves.append(move)
                self._move_count += 1
                return True
        return False

    def check_if_win(self):
        """
        Method checks if game on current map has ended.
        For map to end every target coordinate tile has to be a box
        """
        for row, column in self.targets():
            if self.tiles()[row][column].type() != "box":
                return False
        return True

    def undo_move(self):
        """
        Method undos last made move.
        """
        if self._move_count == 0:
            return None
        move = self._moves.pop()
        player_row, player_column = move.player_was_at()
        player_to_row, player_to_column = move.player_moves_to()
        if move.type() == "normal":
            swap_tiles(self.tiles()[player_row][player_column], self.tiles()[player_to_row][player_to_column])
        elif move.type() == "box_move":
            box_to_row, box_to_column = move.box_moves_to()
            swap_tiles(self.tiles()[player_to_row][player_to_column], self.tiles()[box_to_row][box_to_column])
            swap_tiles(self.tiles()[player_row][player_column], self.tiles()[box_to_row][box_to_column])
        self._move_count -= 1
