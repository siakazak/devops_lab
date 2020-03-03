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
        lst.insert(int(c.split()[1]), int(c.split()[2]))
    elif re.match("^append [0-9]+", c):
        lst.append(int(c.split()[1]))
    elif re.match("^remove [0-9]+", c):
        lst.remove(int(c.split()[1]))
