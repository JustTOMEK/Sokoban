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
    """
    def __init__(self, file_location):
        map_file = open(file_location, "r")
        self._start_map = [line.split() for line in map_file]
        map_file = open(file_location, "r")
        self.current_map = [line.split() for line in map_file]
        self._targets = self.target_coordinates()

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
        if row not in range(0, 10) or column not in range(0, 10):
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
        # check up
        if self.check_coordinates([row - 1, column]) == 'F':
            moves.append([row - 1, column])
            moves.append('U')
        elif self.check_coordinates([row - 1, column]) == 'B' and self.check_coordinates([row - 2, column]) == 'F':
            moves.append([row - 1, column])
            moves.append('U')
        # check right
        if self.check_coordinates([row, column + 1]) == 'F':
            moves.append([row, column + 1])
            moves.append('R')
        elif self.check_coordinates([row, column + 1]) == 'B' and self.check_coordinates([row, column + 2]) == 'F':
            moves.append([row, column + 1])
            moves.append('R')
        # check down
        if self.check_coordinates([row + 1, column]) == 'F':
            moves.append([row + 1, column])
            moves.append('D')
        elif self.check_coordinates([row + 1, column]) == 'B' and self.check_coordinates([row + 2, column]) == 'F':
            moves.append([row + 1, column])
            moves.append('D')
        # check left
        if self.check_coordinates([row, column - 1]) == 'F':
            moves.append([row, column - 1])
            moves.append('L')
        elif self.check_coordinates([row, column - 1]) == 'B' and self.check_coordinates([row, column - 2]) == 'F':
            moves.append([row, column - 1])
            moves.append('L')
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
                row_to_move_to = row - self.player_position[0]
                column_to_move_to = column - self.player_position[1]
                self.current_map[row + row_to_move_to][column + column_to_move_to] = 'b'
            self.current_map[self.player_position[0]][self.player_position[1]] = 'f'
            self.current_map[row][column] = 'p'
            return True
        return False

    def check_if_win(self):
        """
        Method checks if game on current map has ended.
        For map to end boxes have to be on every targer coordinate
        """
        for coordinates in self._targets:
            if self.check_coordinates(coordinates) != "B":
                return False
        return True

    def display_map(self):
        """
        Method prints current map for console presentation.
        """
        for row in self.current_map:
            print(row)
