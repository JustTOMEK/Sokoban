from map import Map


def test_map_create():
    new_map = Map("maps/map_1.txt")
    assert new_map._start_map == new_map.current_map


def test_map_create_row():
    new_map = Map("maps/map_1.txt")
    row_0 = ['w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w', 'w']
    assert new_map._start_map[0] == row_0
    assert new_map.current_map[0] == row_0


def test_player_position():
    new_map = Map("maps/map_1.txt")
    assert new_map.player_position == [4, 5]


def test_available_moves():
    new_map = Map("maps/map_1.txt")
    assert new_map.available_moves() == [[3, 5], 'U', [5, 5], 'D', [4, 4], 'L']


def test_check_coordinates():
    new_map = Map("maps/map_1.txt")
    assert new_map.check_coordinates([0, 0]) == 'W'
    assert new_map.check_coordinates([4, 5]) == 'P'
    assert new_map.check_coordinates([4, 4]) == 'B'
    assert new_map.check_coordinates([10, 10]) == 'W'


def test_move():
    new_map = Map("maps/map_1.txt")
    assert new_map.move("D") is True
    assert new_map.move("R") is False
    assert new_map.move("U") is True
    assert new_map.move("U") is True
    assert new_map.move("L") is False
    assert new_map.move("D") is True
    assert new_map.move("L") is True
    assert new_map.move("D") is False
    assert new_map.move("L") is True
    assert new_map.move("L") is False
    assert new_map.move("R") is True
    assert new_map.move("D") is False
    assert new_map.move("U") is True
    assert new_map.move("L") is False
    assert new_map.move("U") is True
    assert new_map.move("D") is True
    assert new_map.move("R") is True
    assert new_map.move("R") is True


def test_moves_current_move():
    new_map = Map("maps/map_1.txt")
    moves_to_make = ["D", "R", "U", "U", "L", "D", "L", "D", "L",
                     "L", "R", "D", "U", "L", "U", "D", "R", "R"]
    for move in moves_to_make:
        new_map.move(move)
    moves_actually_made = [("D", "B"), ("U", "N"), ("U", "N"), ("D", "N"),
                           ("L", "B"), ("L", "B"), ("R", "N"), ("U", "B"),
                           ("U", "B"), ("D", "N"), ("R", "N"), ("R", "B")]
    assert new_map._moves == moves_actually_made
    assert new_map._move_count == 12


def test_target_coordinates():
    new_map = Map("maps/map_1.txt")
    assert new_map._targets == [[1, 4], [3, 7], [4, 2], [6, 5]]


def test_check_if_win():
    new_map = Map("maps/map_1.txt")
    assert new_map.check_if_win() is False
    assert new_map.move("D") is True
    assert new_map.move("U") is True
    assert new_map.move("L") is True
    assert new_map.move("L") is True
    assert new_map.move("R") is True
    assert new_map.move("U") is True
    assert new_map.move("U") is True
    assert new_map.move("D") is True
    assert new_map.move("R") is True
    assert new_map.move("R") is True
    assert new_map.check_if_win() is True


def test_undo_move():
    new_map = Map("maps/map_1.txt")
    new_map.move("D")
    new_map.move("R")
    new_map.move("U")
    new_map.move("U")
    new_map.undo_move()
    new_map.undo_move()
    new_map.undo_move()
    assert new_map.undo_move() is None
    assert new_map.player_position == [4, 5]
    assert new_map._move_count == 0


def test_redo_move():
    new_map = Map("maps/map_1.txt")
    new_map.redo_move()
    new_map.move("D")
    new_map.move("R")
    new_map.move("U")
    new_map.move("U")
    new_map.undo_move()
    new_map.undo_move()
    new_map.undo_move()
    new_map.redo_move()
    new_map.redo_move()
    new_map.redo_move()
    new_map.redo_move()
    assert new_map._move_count == 3