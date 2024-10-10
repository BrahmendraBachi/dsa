#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'minimumLoss' function below.
#
# The function is expected to return an INTEGER.
# The function accepts LONG_INTEGER_ARRAY price as parameter.
#

from dummy import get_LongText

def minimumLoss(price):
    curr_min = None
    n = len(price)
    price_dict = {}
    for i in range(n):
        price_dict[price[i]] = i
    price_copy = [price[i] for i in range(n)]
    price_copy.sort()

    def find_index(target, l, r):
        if l > r:
            return -1
        m = (l + r) // 2
        if price_copy[m] == target:
            return m
        elif price_copy[m] < target:
            return find_index(target, m + 1, r)
        else:
            return find_index(target, l, m - 1)

    for i in range(n):
        del price_dict[price[i]]
        ind = find_index(price[i], 0, n - 1)
        ind -= 1
        while ind > -1:
            if price_copy[ind] in price_dict:
                if curr_min is None or curr_min < (price_copy[ind] - price[i]):
                    curr_min = price_copy[ind] - price[i]
                break
            else:
                ind -= 1
    return abs(curr_min) if curr_min is not None else 0

    # Write your code here


if __name__ == '__main__':
    input1 = get_LongText().split(" ")
    for i in range(len(input1)):
        input1[i] = int(input1[i])

    # print("1 1 1".split())
    print(minimumLoss(input1))