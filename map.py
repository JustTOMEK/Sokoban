class Map:
    """
    Class map.
    Takes file_location, that is str representing file path.
    Contains attributes:

    :param start_map: start of a level map never changes
    :type start_map: list of lists

    :param current_map: current state of a map
    :type current_map: list of lists

    :param targets: targets at start map
    :type current_map: list of lists

    :param moves: moves made so far in the game
    :type moves: list of touples

    :param move_count: number of moves made
    :type move_count: int

    :param rows: number of rows
    :type rows: int

    :param columns: number of columns
    :type columns: int
    """
    def __init__(self, file_location):
        map_file = open(file_location, "r")
        self._start_map = [line.split() for line in map_file]
        map_file = open(file_location, "r")
        self.current_map = [line.split() for line in map_file]
        self._rows = len(self._start_map)
        self._columns = len(self._start_map[0])
        self._targets = self.target_coordinates()
        self._moves = []
        self._move_count = 0

    @property
    def player_position(self):
        """
        :property player_position: position of a player
        :type player_position: two element list [row, column]
        """
        for number, row in enumerate(self.current_map):
            if 'p' in row:
                return [number, row.index('p')]
            elif 'P' in row:
                return [number, row.index('P')]

    def check_coordinates(self, coordinates):
        """
        Checks what is at given coordinates.
        Returns char if coordinates out of map returns floor.
        Returns uppercase char.
        """
        row, column = coordinates
        if row not in range(0, self._rows) or column not in range(0, self._columns):
            return 'W'
        return self.current_map[row][column].upper()

    def target_coordinates(self):
        """
        Method target_coordinates, check where are targets
        Returns list of coordinates  that are targets
        [[0,1], [0,2], [3,0]]
        """
        targets = []
        for row_number, row in enumerate(self._start_map):
            for column_number, tile in enumerate(row):
                if tile.isupper():
                    targets.append([row_number, column_number])
        return targets

    def available_moves(self):
        """
        Method available_moves, check what moves can player name
        Returns list of coordinates player can go to and direction
        [[0,1], 'R', [0,2], 'L', [3,0], 'U']
        Checks in order up, right, down, left
        """
        row, column = self.player_position
        moves = []
        # directions list contains what coordinate player moves and box moves
        directions = [['U', [-1, 0], [-2, 0]], ['R', [0, 1], [0, 2]],
                      ['D', [1, 0], [2, 0]], ['L', [0, -1], [0, -2]]]
        for direction in directions:
            direction, player, box = direction
            condition_1 = self.check_coordinates([row + player[0], column + player[1]]) == 'F'
            condition_2 = self.check_coordinates([row + player[0], column + player[1]]) == 'B'
            condition_3 = self.check_coordinates([row + box[0], column + box[1]]) == 'F'
            if condition_1 or (condition_2 and condition_3):
                moves.append([row + player[0], column + player[1]])
                moves.append(direction)
        return moves

    def move(self, direction):
        """
        Method moves player in given direction if move is legal.
        If move involves moving box, it will also move box.
        Takes char direction U, R, D, L
        """
        moves = self.available_moves()
        if direction in moves:
            row, column = moves[moves.index(direction) - 1]
            if self.check_coordinates([row, column]) == "B":
                row_move = row - self.player_position[0]
                column_move = column - self.player_position[1]
                self.current_map[row + row_move][column + column_move] = "b"
                self._moves.append((direction, "B"))
            else:
                self._moves.append((direction, "N"))
            self.current_map[self.player_position[0]][self.player_position[1]] = "f"
            self.current_map[row][column] = "p"
            self._move_count += 1
            return True
        return False
    
    def change_box_coordinates(self):
        """
        Method changes current_state after every move.
        It makes target tiles capital letter.
        It makes other tiles lower letter.
        """
        for row_number, row in enumerate(self.current_map):
            for column_number, tile in enumerate(row):
                if [row_number, column_number] in self._targets:
                    if tile.islower():
                        self.current_map[row_number][column_number] = tile.upper()
                elif tile.isupper():
                    self.current_map[row_number][column_number] = tile.lower()

    def check_if_win(self):
        """
        Method checks if game on current map has ended.
        For map to end boxes have to be on every targer coordinate
        """
        for coordinates in self._targets:
            if self.check_coordinates(coordinates) != "B":
                return False
        return True

    def undo_move(self):
        """
        Method undos last made move.
        """
        if self._move_count == 0:
            return None
        directions = {'U': [1, 0], 'R': [0, -1], 'D': [-1, 0], 'L': [0, 1]}
        direction = self._moves[len(self._moves)- self._move_count - 1]
        row, column = self.player_position[0], self.player_position[1]
        if direction[1] == "B":
            self.current_map[row][column] = "b"
            row_to_floor = row + directions[direction[0]][0] * -1
            column_to_floor = column + directions[direction[0]][1] * -1
            self.current_map[row_to_floor][column_to_floor] = "f"
        else:
            self.current_map[row][column] = "f"
        row_to_player = row + directions[direction[0]][0]
        column_to_player = column + directions[direction[0]][1]
        self.current_map[row_to_player][column_to_player] = "p"
        self._moves.pop()
        self._move_count -= 1

    def display_map(self):
        """
        Method prints current map for console presentation.
        """
        for row in self.current_map:
            row_in_str = ''
            for tile in row:
                row_in_str += f'{tile} '
            print(row_in_str)
