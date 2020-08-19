from timeit import timeit
from pprint import pprint
from random import randrange


# Iterating through a strong using loop
# list1 = []
# for x in 'maninder':
#     list1.append(x)
# print(list1)  # result: ['m', 'a', 'n', 'i', 'n', 'd', 'e', 'r']

# there is another way to solve this that is list comprehension, one line of code

# result: ['m', 'a', 'n', 'i', 'n', 'd', 'e', 'r']
list_comp = [x for x in 'maninder']

# 0-9 looping numbers
one = [x for x in range(10)]

# only show range values those divided by two
two = [x for x in range(1, 21) if x % 2 == 0]

# only show range values those divided by three or two
three = [x for x in range(1, 21) if x % 2 == 0 or x % 3 == 0]

# multiple inside the list
four = [x*x for x in range(10)]

five = [x**x for x in range(10)]

six = [x ** 2 for x in range(1, 11)]

seven = [x**2 for x in [x**2 for x in range(1, 11)]]
print(seven)

# Using lambda function inside list
list_lambda = list(map(lambda x: x, 'hello'))

# looping inside list-comp...
obj = ["Even" if i % 2 == 0 else "Odd" for i in range(10)]

price = [1.5, -1.6, -0.5, 6.8, -5, -6, 7, 8, 454, -65, -23, 51, 45, 31, -41]
obj1 = [x if x > 0 else 0 for x in price]  # show only +values


def get_price(num):
    if num > 0:
        return num
    else:
        return 0


# use function inside of list-comp...
obj2 = [get_price(i) for i in price]


matrix = [[1, 2], [3, 4], [5, 6], [7, 8]]
list_matrix = [[row[i] for row in matrix] for i in range(2)]

theline = 'this is a line for test.'
vowels = [x for x in theline if x in 'aeiou']

celsius = [0, 10, 20.5, 35.6, 48.6]
fahrenheit = [((9/5)*temp+32) for temp in celsius]

# Dictionary Comprehensions

quote = "String of some listed words."
vowels1 = {d for d in quote if d in 'aeiou'}

square = {i: i*i for i in range(10)}

# walrus Operator


def get_wether_data():
    return randrange(90, 110)


hot_temp = [temp for _ in range(20) if (temp := get_wether_data()) >= 100]


# Nested Comprehensions
names = ['mike', 'tim', 'john', 'guri', 'tommy']
new = {name: [0 for _ in range(7)] for name in names}

# another example
matrix1 = [[i for i in range(5)] for _ in range(5)]


# Flat array
array = [
        [0, 0, 0],
        [1, 1, 1],
        [2, 2, 2]
]

flat = [num for row in array for num in row]

# Choose Generator for large data

list_sum = sum([i * i for i in range(1000)])
list_sum1 = sum(i * i for i in range(100000000))
list_sum2 = sum(map(lambda i: i*i, range(100000000)))


print('*'*50, end="\n\n")


# Check time of all three ways:

tax_rate = 0.50
tax = [randrange(100) for _ in range(100000)]


def get_rate(txn):
    return txn * (1 + tax_rate)


def getRateWithMap():
    return list(map(get_rate, tax))


def getRateWithComprehension():
    return [get_rate(txn) for txn in tax]


def getRateWithLoop():
    prices = []
    for x in tax:
        prices.append(get_rate(x))
    return prices


print('Map Time: ', timeit(getRateWithMap, number=100))
print('Comprehension Time: ', timeit(getRateWithComprehension, number=100))
print('Loop Time: ', timeit(getRateWithLoop, number=100))
