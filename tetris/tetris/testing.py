from scoreboards import Cell, Text
from random import randint

# ---- TESTING -------

def test_block_list():
    c = Cell()
    assert c.block_list == []

def test_block_values():
    cell1 = Cell(0, randint(1, 7), 0, 5)
    assert cell1.next.next_block == range (1,7)
    assert cell1.hold.hold_block == 0
    assert cell1._maxblocks == 5

def test_add_block():
    c = Cell()
    c.addblock(5)
    assert c.block_list == [5]

def test_lock_block():
    c = Cell(0, randint(1, 7), 5, 5)
    c.lockblock()
    assert c.hold.hold_block == 5

def test_score_and_level_value():
    t = Text(1000, 3)
    assert t.score._current_points == 1000
    assert t.round._current_level == 3

def test_set_level():
    t = Text(0, 0)
    t.round.setlvl(4)
    assert t.round._current_level == 4



    