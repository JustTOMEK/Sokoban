from tile import Wall, Floor, Player, Box
from pytest import raises


def test_create_wall():
    new_wall = Wall(False)
    assert not new_wall.can_move_into()


def test_create_wall_target():
    with raises(ValueError):
        Wall(True)


def test_create_wall_no_target():
    new_wall = Wall(False)
    assert not new_wall.is_target()


def test_create_wall_wrong_init():
    with raises(ValueError):
        Wall(0)


def test_create_player():
    new_player = Player(False)
    assert not new_player.can_move_into()


def test_create_player_target():
    new_player = Player(True)
    assert new_player.is_target()


def test_create_player_no_target():
    new_player = Player(False)
    assert not new_player.is_target()


def test_create_player_wrong_init():
    with raises(ValueError):
        Player(1)


def test_create_box():
    new_box = Box(False)
    assert new_box.can_move_into()


def test_create_box_target():
    new_box = Box(True)
    assert new_box.is_target()


def test_create_box_no_target():
    new_box = Box(False)
    assert not new_box.is_target()


def test_create_box_wrong_init():
    with raises(ValueError):
        Box(0)


def test_create_floor():
    new_floor = Floor(False)
    assert new_floor.can_move_into()


def test_create_floor_target():
    new_floor = Floor(True)
    assert new_floor.is_target()


def test_create_floor_no_target():
    new_floor = Floor(False)
    assert not new_floor.is_target()


def test_create_floor_wrong_init():
    with raises(ValueError):
        Floor(1)


def test_set_is_target_wall():
    new_wall = Wall(False)
    with raises(ValueError):
        new_wall.set_is_target(True)


def test_set_is_target_player():
    new_player = Player(False)
    new_player.set_is_target(True)
    assert new_player.is_target()


def test_set_is_target_box():
    new_box = Box(False)
    new_box.set_is_target(True)
    assert new_box.is_target()


def test_set_is_target_floor():
    new_floor = Floor(False)
    new_floor.set_is_target(True)
    assert new_floor.is_target()
