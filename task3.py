#!/bin/env python
# task3

import re

test = str(input())

if re.match("^[0-9]+[+\-/*][0-9]+=[0-9]+$", test):

    # expression before '='
    expr = re.search("^[0-9]+[+\-/*][0-9]+", test)

    # result after '='
    res = re.search("[0-9]+$", test)

    if eval(expr.group()) == int(res.group()):
        print("YES")
    else:
        print("NO")
else:
    print("ERROR")
