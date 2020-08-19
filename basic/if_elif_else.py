# Basic style of if...else

if not True:
    print("it's not True!")
else:
    print("it's True!")

# ------------------------------------------------------------------

x = False

if x:
    print('x is True.')
else:
    print('x is False.')

# ------------------------------------------------------------------

location = 'bank'

if location == 'shop':
    print('you are in shop now.')
elif location == 'bank':
    print(f'you are in {location} now')
elif location == 'airport':
    print('at the airport')
else:
    print('not desination set yet on list.')

# ------------------------------------------------------------------

x = 25
y = 35
z = 25
if x < y:
    print('x is less than y')
else:
    print('x is greater than y')

# ------------------------------------------------------------------
# Short hand if..else

print("X") if x < y else print("Y")
print('X') if x > y else print('=') if x == y else print('Y')

# ------------------------------------------------------------------
# And, Or

if y > x and z < y:
    print('Both are true')

if y > x or z > y:
    print('one statement is true.')

if x > 10:
    print('Above Ten.')
    if x > 20:
        print('also above 20')
    else:
        print('not above 20')

# ------------------------------------------------------------------
# pass statement

if y > x:
    pass
