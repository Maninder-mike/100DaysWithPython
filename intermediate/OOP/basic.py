# this is not a good way to use class

class Rectangle:
    def area(self):
        return self.lenght * self.width


r = Rectangle()

r.lenght, r.width = 13, 8
# print(r.area())

# ----------------------------------------------------
# this is good way to use class


class Rect:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    @staticmethod
    def add_height(height):
        return height
    
    def total(self):
        return self.add_height + self.area


rr = Rect(9, 6)
print(rr.area())
print(rr.add_height(10))
