from move import NormalMove, BoxMove
from pytest import raises


def test_create_move_normal():
    new_move = NormalMove("Up", (0, 0), (1, 2))
    assert new_move.direction() == "Up"
    assert new_move.player_was_at() == (0, 0)
    assert new_move.player_moves_to() == (1, 2)


def test_create_move_wrong_direction():
    with raises(ValueError):
        NormalMove("Dawn", (0, 0), (1, 2))


def test_create_move_wrong_player_moves_to():
    with raises(TypeError):
        NormalMove("Down", (0, 0), (1, 2, 3))


def test_create_move_wrong_player_moves_to_str():
    with raises(TypeError):
        NormalMove("Down", (0, 0), ("1", 2, 3))


def test_create_move_wrong_player_was_at():
    with raises(TypeError):
        NormalMove("Down", (1, 2, 3), (0, 0))


def test_create_move_wrong_player_was_at_str():
    with raises(TypeError):
        NormalMove("Down", ("1", 2, 3), (0, 0))


def test_create_box_move():
    new_move = BoxMove("Left", (0, 0), (1, 2), (3, 4))
    assert new_move.direction() == "Left"
    assert new_move.player_was_at() == (0, 0)
    assert new_move.player_moves_to() == (1, 2)
    assert new_move.box_moves_to() == (3, 4)


def test_create__box_move_wrong_box_moves_to():
    with raises(TypeError):
        BoxMove("Down", (0, 0), (2, 3), [1, 2])


def test_create_move_wrong_box_moves_to_str():
    with raises(TypeError):
        BoxMove("Down", (0, 0), (2, 3), (1, "2"))


def test_create():
    x = 1
    y = 2
    z = 3
    t = 4
    NormalMove("Up", (x + 3, y), (z, t))
