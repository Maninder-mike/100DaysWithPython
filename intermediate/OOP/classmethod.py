class Rect:
    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def area(self):
        return self.lenght * self.width

    @classmethod
    def add_height(cls, height):
        return height


rr = Rect(9, 6)
print(rr.area())
print(rr.add_height(10))