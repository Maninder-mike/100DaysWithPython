# for loop

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
# for x in list1:    # loop with list
# 	print(x)

# ----------------------------------------------

# for x in list1:
#     if x % 2 == 0:
#         print(x)

# ----------------------------------------------

# for x in list1:
#     if x % 2 == 0:
#         print(x)
#     else:
#         print("Odd Number")

# ----------------------------------------------

# list_sum = 0
# for x in list1:
#     list_sum = list_sum + x
#     list_sum += x
# print(list_sum)

# ----------------------------------------------
# Loop with tuple
tup = (1, 2, 3, 4, 5, 6)
list2 = [(1, 2), (3, 4), (5, 6)]

# for t in tup:
# 	print(t)

# for x in list2:
#     for y in x:
#         print(y)  # result: 1,2,3,4,5,6

# for (t1, t2) in list2:
#     print(t1)  # result: 1,3,5

# ----------------------------------------------
# Loop with Dictonary

d = {'k1': 1, 'k2': 2, 'k3': 3}

# for items in d:
# 	print(d)

# for k, v in d.items():
#     print(k)


# print(list(d.keys()))  # show dict... keys in list.
# print(sorted(d.values()))  # short dict with sorted method.

# ----------------------------------------------
# while loop

x = 0
# while x < 10:
#     print('x in currently: ', x)
#     x += 1

# ----------------------------------------------

# while x < 10:
# 	print('x is currently: ', x)
# 	x+=1
# 	if x ==3:
# 		print('x==3')
# 	else:
# 		print('continue')
# 		continue

# ----------------------------------------------


while x < 10:
    print('x is currently: ', x)
    x += 1
    if x == 5:
        break
    else:
        continue
