from map import Map
from pytest import raises
map_in_str = 'w w F w w w\nw w f w w w\nw w b f b F\nF f b p w w\nw w w b w w\nw w w F w w'


def test_map_create():
    new_map = Map(map_in_str)
    assert new_map.columns() == 6
    assert new_map.rows() == 6


def test_create_not_rectangle_map():
    with raises(ValueError):
        Map("w w w\nw w w\n w w w w")


def test_map_first_row():
    new_map = Map(map_in_str)
    row_0 = ['wall', 'wall', 'floor', 'wall', 'wall', 'wall']
    for tile_number, tile in enumerate(new_map.tiles()[0]):
        assert tile.type() == row_0[tile_number]


def test_player_position():
    new_map = Map(map_in_str)
    assert new_map.player_position() == [3, 3]


def test_check_coordinates():
    new_map = Map(map_in_str)
    assert new_map.check_coordinates((0, 0)) == 'wall'


def test_check_coordinates_not_tuple():
    new_map = Map(map_in_str)
    with raises(TypeError):
        new_map.check_coordinates([0, 0])


def test_check_data_not_int():
    new_map = Map(map_in_str)
    with raises(TypeError):
        new_map.check_coordinates((0, "0"))


def test_check_data_too_long():
    new_map = Map(map_in_str)
    with raises(TypeError):
        new_map.check_coordinates((0, 0, 0))


def test_target_coordinates():
    new_map = Map(map_in_str)
    assert new_map._targets == [(0, 2), (2, 5), (3, 0), (5, 3)]


def test_available_moves():
    new_map = Map(map_in_str)
    assert len(new_map.available_moves()) == 3


def test_available_moves_right_illegal():
    new_map = Map(map_in_str)
    for move in new_map.available_moves():
        assert move._direction != "Right"


def test_move_box_move():
    new_map = Map(map_in_str)
    new_map.move("Down")
    assert new_map.tiles()[3][3].type() == "floor"
    assert new_map.tiles()[4][3].type() == "player"
    assert new_map.tiles()[5][3].type() == "box"


def test_move_normal():
    new_map = Map(map_in_str)
    new_map.move("Up")
    assert new_map.tiles()[3][3].type() == "floor"
    assert new_map.tiles()[2][3].type() == "player"


def test_move_if_can_go_in_walls():
    new_map = Map(map_in_str)
    assert new_map.move("Down") is True
    assert new_map.move("Right") is False
    assert new_map.move("Up") is True
    assert new_map.move("Up") is True
    assert new_map.move("Left") is False


def test_check_if_win():
    new_map = Map(map_in_str)
    assert new_map.check_if_win() is False
    assert new_map.move("Down")
    assert new_map.move("Up")
    assert new_map.move("Left")
    assert new_map.move("Left")
    assert new_map.move("Right")
    assert new_map.move("Up")
    assert new_map.move("Up")
    assert new_map.move("Down")
    assert new_map.move("Right")
    assert new_map.move("Right")
    assert new_map.check_if_win() is True


def test_undo_move():
    new_map = Map(map_in_str)
    new_map.move("Down")
    new_map.move("Right")
    new_map.move("Up")
    new_map.move("Up")
    new_map.undo_move()
    new_map.undo_move()
    new_map.undo_move()
    assert new_map.undo_move() is None
    assert new_map.player_position() == [3, 3]
    assert new_map.move_count() == 0


def test_undo_move_case_1():
    new_map = Map(map_in_str)
    new_map.move("Left")
    new_map.move("Left")
    new_map.undo_move()
    new_map.undo_move()
    new_map.move("Down")
    new_map.undo_move()
    assert new_map.check_coordinates((3, 3)) == "player"
    assert new_map.check_coordinates((3, 2)) == "box"
    assert new_map.check_coordinates((3, 1)) == "floor"
    assert new_map.check_coordinates((3, 0)) == "floor"
