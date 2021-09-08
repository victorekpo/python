Update tuples in Python (Add, change, remove items in tuples)
Source: https://note.nkmk.me/en/python-tuple-operation/

Since tuples tuple in Python are immutable sequences, you can not update them. You can not add, change, remove items (elements) in tuples.

tuple represent data that you don't need to update, so you should use list rather than tuple if you need to update it. However, if you really need to update tuple, you can convert it to list, update it, and then turn it back into tuple.

Tuples are immutable
Take the following tuple as an example.

t = (0, 1, 2)

print(t)
# (0, 1, 2)

print(type(t))
# <class 'tuple'>

You can get elements by index [] or slice [:] like lists.

How to slice a list, string, tuple in Python
print(t[0])
# 0

print(t[:2])
# (0, 1)

Tuples are immutable, so you can not assign a new value to an element.

# t[0] = 100
# TypeError: 'tuple' object does not support item assignment

Destructive methods (= methods that update the original object) such as append() in list are not defined in tuple.

# t.append(100)
# AttributeError: 'tuple' object has no attribute 'append'

Concatenate multiple tuples
Tuples are immutable, but you can concatenate multiple tuples with the + operator. At this time, the original object remains unchanged and a new object is generated.

t_add = t + (3, 4, 5)

print(t_add)
# (0, 1, 2, 3, 4, 5)

print(t)
# (0, 1, 2)

Only tuples can be concatenated. It cannot be concatenated with other types such as lists.

# print(t + [3, 4, 5])
# TypeError: can only concatenate tuple (not "list") to tuple

If you want to add only one element, you can concatenate a tuple with one element.

t_add_one = t + (3,)

print(t_add_one)
# (0, 1, 2, 3)

Note that a tuple with one element requires a comma at the end.
https://note.nkmk.me/en/python-tuple-single-empty/

Add / insert items to tuples
If you want to add new items at the beginning or the end, you can concatenate it with the + operator as described above, but if you want to insert new items at any position, you need to convert a tuple to a list.

Convert tuple into list with list().

Convert lists and tuples to each other in Python
l = list(t)

print(l)
# [0, 1, 2]

print(type(l))
# <class 'list'>

Insert an item with insert().

Add an item to a list in Python (append, extend, insert)
l.insert(2, 100)

print(l)
# [0, 1, 100, 2]
https://note.nkmk.me/en/python-list-append-extend-insert/

Convert list into tuple with tuple().

t_insert = tuple(l)

print(t_insert)
# (0, 1, 100, 2)

print(type(t_insert))
# <class 'tuple'>

Change items in tuples
The flow is the same when changing items. Convert tuple to list, update it, and turn it back into tuple.

l = list(t)
l[1] = 100
t_change = tuple(l)

print(t_change)
# (0, 100, 2)

Remove items in tuples
The same flow can be used to remove items.

l = list(t)
l.remove(1)
t_remove = tuple(l)

print(t_remove)
# (0, 2)


