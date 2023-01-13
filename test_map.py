from map import Map
from tile import Wall, Player, Box, Floor
from move import NormalMove, BoxMove
from pytest import raises


def test_map_create():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert new_map.columns() == 6
    assert new_map.rows() == 6


def test_create_not_rectangle_map():
    with raises(ValueError):
        Map("w w w\nw w w\n w w w w")


def test_map_first_row():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    row_0 = [Wall, Wall, Floor, Wall, Wall, Wall]
    for tile_number, tile in enumerate(new_map.tiles()[0]):
        assert isinstance(tile, row_0[tile_number])


def test_player_position():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert new_map.player_position() == (3, 3)


def test_target_coordinates():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert new_map._targets == [(0, 2), (2, 5), (3, 0), (5, 3)]


def test_available_moves():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert len(new_map.available_moves()) == 3


def test_available_moves_right_illegal():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    for move in new_map.available_moves():
        assert move._direction != "Right"


def test_swap_tiles_floor_floor():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.swap_tiles((0, 2), (1, 2))
    assert new_map.tiles()[0][2].is_target()
    assert not new_map.tiles()[1][2].is_target()


def test_swap_tiles_box_floor():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.swap_tiles((1, 2), (2, 2))
    assert isinstance(new_map.tiles()[1][2], Box)
    assert isinstance(new_map.tiles()[2][2], Floor)


def test_swap_tiles_player_floor():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.swap_tiles((3, 3), (2, 3))
    assert isinstance(new_map.tiles()[2][3], Player)
    assert isinstance(new_map.tiles()[3][3], Floor)


def test_swap_tiles_box_floor_targets():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.swap_tiles((2, 4), (2, 5))
    assert not new_map.tiles()[2][4].is_target()
    assert new_map.tiles()[2][5].is_target()


def test_swap_tiles_wrong_coordinates():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    with raises(ValueError):
        new_map.swap_tiles((2, 4), (2, 6))


def test_add_move():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.add_move(NormalMove("Up", (1, 1), (1, 2)))
    new_map.add_move(BoxMove("Up", (1, 3), (1, 4), (1, 5)))
    assert len(new_map.moves()) == 2


def test_delete_move():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.add_move(NormalMove("Up", (1, 1), (1, 2)))
    deleted_move = new_map.delete_last_move()
    assert new_map.move_count() == 0
    assert isinstance(deleted_move, NormalMove)


def test_add_move_wrong_type():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    with raises(ValueError):
        new_map.add_move(Box(True))


def test_move_normal():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert new_map.move("Up")
    assert isinstance(new_map.tiles()[2][3], Player)
    assert isinstance(new_map.tiles()[3][3], Floor)


def test_move_box_move():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert new_map.move("Down")
    assert isinstance(new_map.tiles()[4][3], Player)
    assert isinstance(new_map.tiles()[3][3], Floor)
    assert isinstance(new_map.tiles()[5][3], Box)


def test_move_not_available():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    assert not new_map.move("Right")


def test_check_if_win():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
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
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.move("Down")
    new_map.move("Right")
    new_map.move("Up")
    new_map.move("Up")
    assert new_map.undo_move()
    assert new_map.undo_move()
    assert new_map.undo_move()
    assert new_map.undo_move() is None
    assert new_map.player_position() == (3, 3)
    assert new_map.move_count() == 0


def test_undo_move_case_1():
    map_in_str = ('w w F w w w\nw w f w w w\nw w b f'
                  'b F\nF f b p w w\nw w w b w w\nw w w F w w')
    new_map = Map(map_in_str)
    new_map.move("Left")
    new_map.move("Left")
    new_map.undo_move()
    new_map.undo_move()
    new_map.move("Down")
    new_map.undo_move()
    assert isinstance(new_map.tiles()[3][3], Player)
    assert isinstance(new_map.tiles()[3][2], Box)
    assert isinstance(new_map.tiles()[3][1], Floor)
    assert isinstance(new_map.tiles()[3][0], Floor)
