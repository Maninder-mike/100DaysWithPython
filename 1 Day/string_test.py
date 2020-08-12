
m = 'Mike'


def test_string():
    assert m.capitalize() == 'Mike'
    assert m.center(10) == '   Mike   '
    assert m.endswith("e") != 'e'
