#!/bin/env python
# task4

import re

lst = []
commands = []

# number of commands
num = int(input())

for i in range(num):
    commands.append(input())

for c in commands:
    if c == 'print':
        print(lst)
    elif c == 'sort':
        lst.sort()
    elif c == 'pop':
        lst.pop()
    elif c == 'reverse':
        lst.reverse()
    elif re.match("^insert [0-9]+ [0-9]+", c):
        c = list(c.split(" "))
        lst.insert(int(c[1]), int(c[2]))
    elif re.match("^append [0-9]+", c):
        c = list(c.split(" "))
        lst.append(int(c[1]))
    elif re.match("^remove [0-9]+", c):
        c = list(c.split(" "))
        lst.remove(int(c[1]))
