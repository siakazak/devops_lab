#!/bin/env python
# task2

list1 = input().split()
list2 = input().split()
out = []

for el in set(list1).intersection(set(list2)):
    out.append(int(el))

# sorting int elements works in another way than string ones
out.sort()

# Put elements into a single string
print(' '.join(map(str, out)))
