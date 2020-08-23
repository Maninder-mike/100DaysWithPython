# ------------------Built in functions---------------------------------

# abs()

print("abs() -", abs(-3))
print("abs() -", abs(3 + 5j))

# all()
# Check all items are True else Flase
print("all() -", all([True, True, False]))
print("all() -", all([True, True, True]))
print("all() -", all([0, 0, 1]))  # o,1 are also represent True & Flase
print("all() -", all((0, True, False)))  # all() with tuple
print("all() -", all({0, 1, 1}))  # with set
print("all() -", all({0: "apple", 1: "orange"}))  # with Dictionary

# any()
# Check if one item True else Flase
print("any() -", any((True, False, True)))
print("any() -", any((1, False, 0)))

# ascii
print("ascii() -", ascii(123))  # TODO make it

# bin()
print("bin() -", bin(123))

# bool()
print("bool() -", bool(1))
# empty object is false
print("bool() -", bool(0))
print("bool() -", bool([]))
print("bool() -", bool(()))
print("bool() -", bool({}))
print("bool() -", bool(None))

# bytearray()
print("bytearray() -", bytearray(5))
print("bytearray() -", bytearray("mike", encoding="utf-8"))
print("bytearray() -", bytearray("mike", encoding="utf-16"))

# bytes()
print("bytes() -", bytes(5))
print("bytes() -", bytes("mike", encoding="utf-8"))
print("bytes() -", bytes("mike", encoding="utf-16"))

# callable()


def x():
    a = 5


a = 5

print("callable() -", callable(x))
print("callable() -", callable(a))

# chr()
print("chr() -", chr(5))  # unicode character number

# classmethod()
print("classmethod()")  # TODO classethod

# compile() # TODO learn it
cy = compile("print(88)", "test", "eval")
print("compile() -", exec(cy))

# complex()
print("complex() -", complex(3, 5))
print("complex() -", complex("3+5j"))

# delattr() # TODO learn delattr


class Person:
    name = "mike"
    age = 25
    country = "india"


# delattr(Person, 'age')
print("delattr() -", delattr(Person, "age"))

# dict()
print("dict() -", dict(name="mike", country="india"))

# dir()
print("dir() -", dir(Person))

# divmod()
print("divmod() -", divmod(10, 2))

# enumerate

# for x, y in enumerate('aeiou'):
# for x in enumerate('aeiou', 100):
# print(x, y)

myList = ["apple", "banana", "grapes", "orange"]

print("enumerate() -", list(enumerate(myList, start=10)))

# eval()
print("eval() -", eval("print(55)"))

# filter()

ages = [25, 35, 14, 18, 22]


def findAge(x):
    if x < 20:
        return False
    return True


filterTest = filter(findAge, ages)
for a in filterTest:
    print("filter() -", a)

# float()
print(float(10))
print(float(3.1415))

# format()  # TODO add more examples

print("format() -", format(255, "x"))  # 255 in hexadecimal value
print("format() -", format(0.5, "%"))
print("format() -", format(500, "b"))

# frozenset()
myset = ["ladyfinger", "tomato", "potato"]
frozenset(myset)
myset[1] = "apple"
print(myset)

# getattr()
print("getattr() -", getattr(Person, "name"))
print("getattr() -", getattr(Person, "page", "my message"))

# globals()
print("globals() -", globals())
print("globals() -", globals()["__file__"])

# hasattr()
print("hasattr() -", hasattr(Person, "name"))

# hash()
print("hash() -", hash("this is hash value"))

# help()

# print('help() -', help())

# id()
print("id() -", id(myset))

# input()
# print('input() -', input('this is input: '))

# int()
print("int() -", int(3.1415))

# isinstance() # TODO add more examples...
print("isinstance() -", isinstance(5, int))
print("isinstance() -", isinstance(5, str))
print("isinstance() -", isinstance("hello", (int, str, float, list, dict, tuple)))

# issubclass()


class myJob(Person):
    job = "programmer"


print("issubclass() -", issubclass(myJob, Person))


# iter()
itr = iter(["apple", "banana", "cherry"])
print("iter() -", next(itr))
print("iter() -", next(itr))
print("iter() -", next(itr))

# len()
print("len() -", len(myList))

# locals()
lcl = locals()

print("locals() -", lcl)
print("locals() -", lcl["__file__"])

# map()


def myfunc(m):
    return len(m)


m = map(myfunc, myList)

print("map() -", m)
print("map() -", list(m))

# max()
print("max() -", max(1, 2, 3, 4, 5, 6))
print("max() -", max(myList))

# memoryview()
mv = memoryview(b"Hello")

print("memoryview() -", mv)
print("memoryview() -", mv[0])
print("memoryview() -", mv[1])

# min()
print("min() -", min(1, 2, 3, 4, 5, 6))
print("min() -", min(myList))

# next()
next_itr = iter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print("next() -", next(next_itr))
print("next() -", next(next_itr))
print("next() -", next(next_itr))
print("next() -", next(next_itr))

# object()  # TODO add more...
ob = object()
print("object() -", ob)

# oct()
print("oct() -", oct(123456))

# open()
# 'r':read, 'a':append, 'w':write, 'x':create, 't':text mode, 'b':binary
f = open("sample.txt", "r")
print(f.read())

# ord()
print("ord() -", ord("M"))
print("ord() -", ord("👳"))

# pow()
print("pow() -", pow(5, 2))

# print()
print("print() -", "Hello world!")

# property() # TODO add it...
print("property() -", "not impliment yet!")

# range()
rng = range(1, 6)
print("range() -", range(1, 6))

for r in rng:
    print(r)

# repr()
print("repr() -", repr(myList))

# reversed()
print("reversed() -", reversed([1, 2, 3, 4, 5, 6]))
rev = reversed([1, 2, 3, 4, 5, 6])

for x in rev:
    print(x)

# round()
print("round() -", round(3.1415))
print("round() -", round(3.1415, 2))

# set()
dummy = [54, 5, 1, 51, 1, 21, 21, 3, 123, 4, 5, 32, 3, 2]

print("set() -", set(myList))
print("set() -", set(dummy))

# setattr()
print("setattr() -", setattr(myJob, "job", "driver"))

# slice()
slc = ("a", "b", "c", "d")
print("slice() -", slc[slice(2)])
print("slice() -", slc[slice(3, 6)])

# sorted()
print("sorted() -", sorted(myList))
print("sorted() -", sorted(dummy))

# @staticmethod()
print("@staticmethod() -", "not impliment yet")

# str()
print("str() -", str(123))

# sum()
print("sum() -", sum(dummy))

# super()
class PersonTwo(Person):
    def __init__(self, txt):
        super().__init__(txt)


print("super() -")

# tuple()
print("tuple() -", tuple(dummy))

# type()
print("type() -", type(dummy))
print("type() -", type((1, 2, 3)))
print("type() -", type({1, 2, 3}))
print("type() -", type({1: "one", 2: "two"}))
print("type() -", type("mike"))
print("type() -", type(123))
print("type() -", type(1.2))

# vars()
print("vars() -", vars(Person))
print("vars() -", vars())

# zip()
zp = zip(myList, dummy)
print("zip() -", zp)
for z in zp:
    print(z)

# ------------------------------------------------------------
