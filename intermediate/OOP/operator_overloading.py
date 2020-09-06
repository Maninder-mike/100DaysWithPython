class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    # Overloading the + Operator
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    # TODO work on it.

    def __sub__(self, other):
        pass

    def __mul__(self, other):
        pass

    def __pow__(self, other):
        pass

    def __truediv__(self, other):
        pass

    def __floordiv__(self, other):
        pass

    def __mod__(self, other):
        pass

    def __lshift__(self, other):
        pass

    def __rshift__(self, other):
        pass

    def __and__(self, other):
        pass

    def __or__(self, other):
        pass

    def __xor__(self, other):
        pass

    def __invert__(self, other):
        pass

    # Overloading Comparison Operators
    def __lt__(self, other):
        pass

    def __le__(self, other):
        pass

    def __eq__(self, other):
        pass

    def __ne__(self, other):
        pass

    def __gt__(self, other):
        pass

    def __ge__(self, other):
        pass


p1 = Point(1, 2)
p2 = Point(3, 4)

print(p1)
print(p2)

print(p1+p2)
