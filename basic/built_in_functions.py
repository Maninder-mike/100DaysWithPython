# ------------------Built in functions---------------------------------

# abs()

print('abs() -', abs(-3))
print('abs() -', abs(3+5j))

# all()
# Check all items are True else Flase
print('all() -', all([True, True, False]))
print('all() -', all([True, True, True]))
print('all() -', all([0, 0, 1]))   # o,1 are also represent True & Flase
print('all() -', all((0, True, False)))   # all() with tuple
print('all() -', all({0, 1, 1}))  # with set
print('all() -', all({0: 'apple', 1: 'orange'}))  # with Dictionary

# any()
# Check if one item True else Flase
print('any() -', any((True, False, True)))
print('any() -', any((1, False, 0)))

# ascii
print('ascii() -', ascii(123))   # TODO make it

# bin()
print('bin() -', bin(123))

# bool()
print('bool() -', bool(1))
# empty object is false
print('bool() -', bool(0))
print('bool() -', bool([]))
print('bool() -', bool(()))
print('bool() -', bool({}))
print('bool() -', bool(None))

# bytearray()
print('bytearray() -', bytearray(5))
print('bytearray() -', bytearray('mike', encoding='utf-8'))
print('bytearray() -', bytearray('mike', encoding='utf-16'))

# bytes()
print('bytes() -', bytes(5))
print('bytes() -', bytes('mike', encoding='utf-8'))
print('bytes() -', bytes('mike', encoding='utf-16'))

# callable()


def x():
    a = 5


a = 5

print('callable() -', callable(x))
print('callable() -', callable(a))

# chr()
print('chr() -', chr(5))  # unicode character number

# classmethod()
print('classmethod()')  # TODO classethod

# compile() # TODO learn it
cy = compile('print(88)', 'test', 'eval')
print('compile() -', exec(cy))

# complex()
print('complex() -', complex(3, 5))
print('complex() -', complex('3+5j'))

# delattr() # TODO learn delattr


class Person:
    name = 'mike'
    age = 25
    country = 'india'


# delattr(Person, 'age')
print('delattr() -', delattr(Person, 'age'))

# dict()
print('dict() -', dict(name='mike', country='india'))

# dir()
print('dir() -', dir(Person))

# divmod()
print('divmod() -', divmod(10, 2))

# enumerate

# for x, y in enumerate('aeiou'):
# for x in enumerate('aeiou', 100):
# print(x, y)

myList = ['apple', 'banana', 'grapes', 'orange']

print('enumerate() -', list(enumerate(myList, start=10)))

# eval()
print('eval() -', eval('print(55)'))

# filter()

ages = [25, 35, 14, 18, 22]


def findAge(x):
    if x < 20:
        return False
    return True


filterTest = filter(findAge, ages)
for a in filterTest:
    print('filter() -', a)

# float()
print(float(10))
print(float(3.1415))

# format()  # TODO add more examples

print('format() -', format(255, 'x'))  # 255 in hexadecimal value
print('format() -', format(0.5, '%'))
print('format() -', format(500, 'b'))

# frozenset()
myset = ['ladyfinger', 'tomato', 'potato']
frozenset(myset)
myset[1] = 'apple'
print(myset)

# ------------------------------------------------------------
