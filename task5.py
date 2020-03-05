#!/bin/env python
# task5 from Homework2: Siarhei Kazak


def sd_in_range(nrange):
    out = []
    for number in range(int(nrange[0]), int(nrange[1]) + 1):

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

    return out

if __name__ == "__main__":
    sd_nums = sd_in_range(input().split())
    print(sd_nums)
