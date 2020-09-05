
class Person:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    def fullName(self):
        return self.first, self.last


class Age:
    def __init__(self, age):
        self.age = age


class Student(Person):    # first child style
    pass


class Student1(Person, Age):     # second child style
    def __init__(self, first, last, age):
        Person.__init__(self, first, last)
        Age.__init__(self, age)

    def stdAge(self):
        return self.first, self.last, self.age


class Student2(Person):       # third child style
    def __init__(self, first, last, batch):
        super().__init__(first, last)
        self.batch = batch

    def fullName(self):   # add another fullName methond in child class.
        return self.first, self.last, self.batch


one = Person("mike", "time")
std = Student("john", "sammy")

std1 = Student1("tommy", "manny", 25)
std1age = Student1("ramy", "yanky", 28)

std2 = Student2("nile", "santhos", 2020)


print(one.fullName())
print(std.fullName())

print(std1.fullName())
print(std1age.stdAge())

print(std2.fullName())
