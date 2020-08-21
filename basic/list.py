thelist = [0, 'one', 'two', 'three', 'four', 5, 6, 'seven', 8, 'nine', 10]
list2 = [1, 2, 3, 4, 5]
list3 = thelist.copy()  # Copy list with all values
list4 = thelist + list2  # join two list and make another list

# print(thelist[1])
# print(thelist[-1])
# print(thelist[1:3])
# print(thelist[2:])
# print(thelist[-5:-1])
# print(thelist[::-1])

# print(thelist*2)
# print(len(thelist))  # Check lenght

# thelist[0] = 'Zero'  # Change value in list

# thelist.append('add item')  # for add item in the last
# thelist.extend(list2)  # add another list in it.
# list2.sort()  # sort the value but if value only str or int, not together
# list2.reverse() # reverce all values in the list
# print(thelist.pop())  # remove the  last value or asign value
# print(thelist.pop(2))
# thelist.remove('two')  # remove specific value
# print(thelist.count('one'))  # total same items in list
# print(thelist.index('three'))  # Check index of the value in the list
# print(thelist.index('three', 5, 9)) # Check index of the value with asign location
# print(thelist.clear())  # cleat all items form the list

# thelist.insert(2, 'second value')  # insert value with postion

# for x in thelist:
#     print(x)  # show list by loop

# if 'one' in thelist:   # check if value in the list
#     print('One is in the list')
# else:
#     print("not in it.")

print(list('abcdef'))

mylist = [1, 2, 3, 4, 5]
mylist1 = ['a', 'b', 'c', 'd', 'e']

print(list(zip(mylist, mylist1)))
