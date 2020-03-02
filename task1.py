#!/bin/env python
# task1

year = int(input())


def is_leap(yr):
    if yr % 400 == 0:
        print("True")
    elif yr % 100 == 0:
        print("False")
    elif yr % 4 == 0:
        print("True")
    else:
        print("False")

is_leap(year)
