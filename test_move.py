from move import Move
from pytest import raises


def test_create_move_normal():
    new_move = Move("normal", "Up", (0, 0), (1, 2))
    assert new_move.type() == "normal"
    assert new_move.player_moves_to() == (1, 2)
    assert new_move.direction() == "Up"


def test_create_box_move():
    new_move = Move("box_move", "Up", (0, 0), (1, 2), (3, 4))
    assert new_move.type() == "box_move"
    assert new_move.player_moves_to() == (1, 2)
    assert new_move.box_moves_to() == (3, 4)
    assert new_move.direction() == "Up"


def test_create_move_wrong_type():
    with raises(ValueError):
        Move("box_mowe", "Down", (0, 0), (1, 2), (3, 4))


def test_create_move_wrong_direction():
    with raises(ValueError):
        Move("box_move", "Dawn",  (0, 0), (1, 2), (3, 4))


def test_create_move_wrong_player_moves_to():
    with raises(TypeError):
        Move("normal", "Down", (0, 0), (1, 2, 3))


def test_create_move_wrong_player_moves_to_str():
    with raises(TypeError):
        Move("normal", "Down", (0, 0), ("1", 2, 3))


def test_create_move_wrong_box_moves_to():
    with raises(TypeError):
        Move("box_move", "Down", (0, 0), (2, 3), [1, 2])


def test_create_move_wrong_box_moves_to_str():
    with raises(TypeError):
        Move("box_move", "Down", (0, 0), (2, 3), (1, "2"))


def test_create_move_wrong_player_was_at():
    with raises(TypeError):
        Move("normal", "Down", (1, 2, 3), (0, 0))


def test_create_move_wrong_player_was_at_str():
    with raises(TypeError):
        Move("normal", "Down", ("1", 2, 3), (0, 0))
