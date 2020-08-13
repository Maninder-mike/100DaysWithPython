tup = (1, 5, 'time', 3.1415, "Mike", 1, 'time', 5, 475, 5)


def test_tuple():
    assert tup.count('time') == 2
    assert tup.count(5) == 3

    assert tup.index('time') == 2
    assert tup.index(5) != 2

    assert tup.index(5) <= 10
