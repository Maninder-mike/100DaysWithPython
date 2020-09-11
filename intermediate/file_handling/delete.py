from os import path, remove

if path.exists('write_new.txt'):
    remove('write_new.txt')
else:
    print("The file does not exist.")
