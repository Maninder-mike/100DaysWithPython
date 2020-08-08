

def test_string():
    assert 'Mike'.capitalize() == 'Mike'
    assert 'mike'.center(10) == '   mike   '
    assert 'Mike'.endswith("e") != 'e'
