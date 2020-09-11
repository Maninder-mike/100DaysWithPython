m = 'Mike'
n = 'this is a string for test.'


def test_string():
	assert m.capitalize() == 'Mike'
	assert m.center(10) == '   Mike   '

	assert m.lower() == 'mike'
	assert m.title() == 'Mike'

	assert m.upper() == 'MIKE'
	assert m.count('Mike') == 1

	assert m.index('Mike') == 0
	assert m.count('M') == 1

	assert n.endswith('.') == True
	assert n.startswith('this') == True
