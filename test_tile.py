from tile import Tile, swap_tiles
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
    new_tile.set_type("wall")
    assert new_tile.type() == "wall"


def test_set_wrong_type():
    new_tile = Tile("F")
    with raises(ValueError):
        new_tile.set_type("F")


def test_set_wall_target():
    new_tile = Tile("F")
    with raises(ValueError):
        new_tile.set_type("W")


def test_swap_tiles():
    tile_1 = Tile("F")
    tile_2 = Tile("p")
    swap_tiles(tile_1, tile_2)
    assert tile_1.type() == "player"
    assert tile_2.type() == "floor"
    assert tile_1.is_target()
    assert not tile_2.is_target()


def test_swap_not_wall_with_wall():
    tile_1 = Tile("F")
    tile_2 = Tile("w")
    with raises(ValueError):
        swap_tiles(tile_1, tile_2)
