# Iterator in Classes with built in '__iter__', '__next__'

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

    def loop(self, x):
        return [i for i in x]


rev = Reverse("maninder")
print(rev.loop(rev))
