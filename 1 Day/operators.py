print('Arithmetic Operators')

print('Addition', 1 + 2)
print('Subtraction', 1 - 2)
print('Multiplication	', 2 * 2)
print('Division', 7 / 2)
print('Modulus', 7 % 2)
print('Exponentiation', 2 ** 2)
print('Floor division', 7 // 2)

print('Assignment Operators')
x = 2
print('x=2 =', x)
x += 3
print('x+=3 =', x)
x -= 2
print('x-=2 =', x)
x *= 3
print('x*=3 =', x)
x /= 2
print('x/=2 =', x)
x %= 3
print('x%=3 =', x)
x //= 0.5
print('x//-=2 =', x)
x **= 3
print('x**=3 =', x)
x = 50
x &= 2
print('x&=2 =', x)
x |= 3
print('x|=3 =', x)
x ^= 3
print('x^=3 =', x)
x >>= 3
print('x>>=3 =', x)
x <<= 3
print('x<<=3 =', x)

print('Comparison Operators')

print('5 == 6 : ', 5 == 6)
print('5 != 6 : ', 5 != 6)
print('5 > 6 : ', 5 > 6)
print('5 < 6 : ', 5 < 6)
print('5 >= 6 : ', 5 >= 6)
print('5 <= 6 : ', 5 <= 6)

print('Logical Operators')

print('x < 5 and  x < 10 :', x < 5 and x < 10)
print('x < 5 or x < 4 :', x < 5 or x < 4)
print('not(x < 5 and x < 10) :', not(x < 5 and x < 10))

print('Identity Operators')
x = ["apple", "banana"]
y = ["apple", "banana"]

print('z = x :', x is y)
print('z = x :', x is not y)


print('Membership Operators')
fruit = ["apple", "banana"]

print("'banana' in fruit :", 'banana' in fruit)
print("'banana' not in fruit :", 'banana' not in fruit)

print('Bitwise Operators')
print('&')
print('|')
print('^')
print('~')
print('<<')
print('>>')
