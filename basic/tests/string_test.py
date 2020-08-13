
m = 'Mike'


def test_string():
    assert m.capitalize() == 'Mike'
    assert m.center(10) == '   Mike   '
    assert m.endswith("e") != 'e'
    assert m.lower() == 'mike'
    assert m.title() == 'Mike'

    assert m.upper() == 'MIKE'
    assert m.count('Mike') == 1

    assert m.index('Mike') == 0
