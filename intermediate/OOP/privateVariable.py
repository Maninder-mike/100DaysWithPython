# __private '__' add security in declaried vaiables. those are not use out side the other class.

class Passwords:
    def __init__(self):
        self.__database = []

    def addPass(self, n):
        return self.__database.append(n)

    def showPasswords(self):
        showdata = self.__database
        return showdata


pp = Passwords()

print(pp.addPass("Tpass."))
print(pp.addPass("1223455"))
print(pp.addPass("noshowpass"))

print(pp.showPasswords())
