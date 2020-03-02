#!/bin/env python
# task5

inp = input().split(" ")
out = []

for number in range(int(inp[0]), int(inp[1]) + 1):

    # string for storing digits
    tmp = ""

    for digit in str(number):

        # avoid division by 0
        if int(digit) == 0:
            break

        # store valid digit into string
        if number % int(digit) == 0:
            tmp += digit

    # compare valid string with initial one
    if str(number) == tmp:
        out.append(number)

print(out)
