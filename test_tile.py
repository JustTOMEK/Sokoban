from tile import Tile
from pytest import raises


def test_create_tile_upper_char():
    new_tile = Tile("f")
    assert new_tile.type() == "floor"


def test_create_tile_lower_char():
    new_tile = Tile("F")
    assert new_tile.type() == "floor"


def test_create_wall_target():
    with raises(ValueError):
        Tile("W")


def test_create_tile_string():
    with raises(TypeError):
        Tile("floor")


def test_create_wrong_tile():
    with raises(TypeError):
        Tile("z")


def test_create_tile_int():
    with raises(TypeError):
        Tile(123)


def test_is_not_target():
    new_tile = Tile("f")
    assert not new_tile.is_target()


def test_is_target():
    new_tile = Tile("F")
    assert new_tile.is_target()


def test_set_type():
    new_tile = Tile("F")
    new_tile.set_type("w")
    assert new_tile.type() == "wall"


def test_set_wrong_type():
    new_tile = Tile("F")
    with raises(TypeError):
        new_tile.set_type("z")


def test_set_wall_target():
    new_tile = Tile("F")
    with raises(ValueError):
        new_tile.set_type("W")


def test_change_is_target():
    new_tile = Tile("f")
    assert not new_tile.is_target()
    new_tile.set_type("B")
    assert new_tile.is_target()
