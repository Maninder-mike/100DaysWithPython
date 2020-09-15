# Python container datatype
from collections import ChainMap, Counter, defaultdict, deque, namedtuple, UserDict, UserList, UserString, OrderedDict

# ChainMap -------------------------------

baseline = {'music': 'pop', 'art': 'modren'}
adjustments = {'art': 'rock', 'opera': 'carmen'}

print('ChainMap list \t: ', list(ChainMap(adjustments, baseline)))

# Counter --------------------------------
print()

cnt = Counter()

for word in ['red', 'blue', 'red', 'green', 'blue', 'blue']:
    cnt[word] += 1
print('Counter, word count \t: ', cnt)

c = Counter(a=4, b=2, c=0, d=2)
d = Counter(a=1, b=2, c=3, d=4)
print('Counter all elements \t : ', sorted(c.elements()))

print('Counter most common \t : ', (c.most_common(2)))

c.subtract(d)
print('Counter subtract \t : ', c)

print('Counter sum\t :', sum(d.values()))
print('Counter list\t :', list(c))
print('Counter set\t :', set(c))
print('Counter dict\t :', dict(c))

# defaultdict ----------------------------
print()

s = [('yellow', 2), ('pink', 6), ('red', 10), ('green', 3), ('majenta', 5)]

d = defaultdict(list)

for k, v in s:
    d[k].append(v)

print('defaultdict sorted\t : ', sorted(d.items()))

n = 'maninder'

dd = defaultdict(int)
for k in n:
    dd[k] += 1

print('defaultdict sorted\t : ', sorted(dd.items()))

# deque ----------------------------------
print()

d = deque('mike')
print('deque normel \t :', d)

d.append('j')
print('deque append \t :', d)

d.appendleft('f')
print('deque appendleft \t :', d)

d.pop()  # remove right most item
print('deque pop \t :', d)

d.popleft()  # remove left most item
print('deque popleft \t :', d)

e = d.copy()  # remove left most item
print('deque shallow copy \t :', e)

# e.remove() # delete deque
# print('deque delete \t :', e)

print('deque count element \t :', d.count('m'))

print('deque reversed items \t :', list(reversed(d)))

# namedtuple() ---------------------------
print()

Point = namedtuple('Point', ['x', 'y'])
p = Point(11, y=22)

print('namedtuple \t : ', p)
print('namedtuple sum \t : ', p[0] + p[1])

x, y = p
print('namedtuple unpacking \t : ', x, y)

# OrderDict ------------------------------
print()

d = OrderedDict.fromkeys('abcdef')
print('OrderedDict Normal \t : ', d)

d.move_to_end('a')
print('OrderedDict move_to_end \t : ', d)

# UserDict -------------------------------
print()

ud = {'a': 1,
      'b': 2,
      'c': 3}

uDict = UserList(ud)
print('UserDict \t : ', uDict.data)

# UserList -------------------------------
print()

L = [1, 2, 3, 4]

userL = UserList(L)
print('UserList \t : ', userL.data)

# UserString -----------------------------
print()

d = 'this is a string.'

userS = UserString(d)
print('UserString \t : ', userS.data)
