print("Place holder using the module % charater.".center(50, '-'))

print("I'm a %s programmer." % 'Smart')
print("Those %s are very %s." % ('birds', 'beautiful'))

x, y = 10, 15
print("%d + %d = %d" % (x, y, x+y))

print("str() %s" % 'Mike')
print("repr() %r" % 'Mike')

print("I write %s here" % 3.1415)
print("I write %d here" % 3.1415)

print("Floating number:%5.2f" % (13.1415))
print("Floating number:%1.0f" % (13.1415))
print("Floating number:%1.5f" % (13.1415))
print("Floating number:%10.2f" % (13.1415))
print("Floating number:%25.2f" % (13.1415))

print("First:%s, Second:%5.2f, Third:%r" % ('Hi', 3.1415, 'bye'))


print(".format() string method".center(50, '-'))

print("This is format strong with {}.".format('insert'))
print("{},{},{}".format('One', 'two', 'three'))
print("First:{a},Second:{b},Three{c}".format(a='1st', b='2nd', c='3rd'))
print("{a},{b},{c}".format(b=2, c=1.5, a=1))

# Alinement, Padding, and Precision with .format()
print('{0:8} | {1:9}'.format('fruit', 'quantity'))
print('{0:8} | {1:9}'.format('apple', '10'))
print('{0:8} | {1:9}'.format('banana', '50'))

print('{0:<8} | {1:^8} | {2:>8}'.format('left', 'center', 'right'))
print('{0:<8} | {1:^8} | {2:>8}'.format(11, 22, 33))
print('{0:<8} | {1:^8} | {2:>8}'.format(1.5, 25, 55))

print('{0:=<8} | {1:-^8} | {2:.>8}'.format('left', 'center', 'right'))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(11, 22, 33))
print('{0:=<8} | {1:-^8} | {2:.>8}'.format(99, 88, 77))

print("formating with f-string".center(50, '-'))

name = 'mike'

print(f"this is f string {name}")
print(f"this is f string {name!r}")

num = 3.1415
print(f"10 Character, four decimal: {num:{10}.{6}}")

print(f"10 Character, four decimal: {num:10.4f}")
