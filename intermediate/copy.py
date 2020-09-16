# Shallow and deep copy operations
from copy import copy, deepcopy

# -------------------------------------------------------------------------
old_list = [1, 2, 3, 4, 5, 6, [7, 8, 9]]
new_list = old_list

print('Old List :', old_list)
print('Old List id :', id(old_list))

print()

print('New List :', new_list)
print('New List id:', id(new_list))
# -------------------------------------------------------------------------
print('Shallow Copy')

new_list2 = copy(new_list)
print('New List 2 :', new_list2)

new_list.append('added')

print('New List 2 :', new_list2)
# -------------------------------------------------------------------------
# this make independent object if x = y, x changed than not changes in y
print('Deep Copy')

m = [1, 2, 3]
n = deepcopy(m)
print(m)
print(n)
