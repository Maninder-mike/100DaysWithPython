# 'r': read, 'a': append, 'w': write, 'x': create
# 't': default value text, 'b': binart mode

demo_file = open('demo.txt')  # Default reading mode.

print(demo_file)
print(demo_file.read())  # read ifle and add number of value.
demo_file.close()

# -----------------------------------------------------------------------------------
demo_file2 = open('demo.txt', 'rt')  # Default reading mode with text.
# if value in readable
print('is file is readable: ', demo_file2._checkReadable())
print(demo_file2.readline())
print(demo_file2.readline())
print(demo_file2.readline())
demo_file2.close()  # without this line file is still open in program could be lost data

# -----------------------------------------------------------------------------------
# Or loop through

f = open('demo.txt')
for x in f:
    print(x, end="")

# -----------------------------------------------------------------------------------
# open file 'with' function
print("\n\nWith Function: \n")
with open('demo.txt', 'r') as f:
    read = f.read()   # no need close() function with handle itself.
print(read)
# -----------------------------------------------------------------------------------
