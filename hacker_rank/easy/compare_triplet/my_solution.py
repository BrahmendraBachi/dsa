import math
import os
import random
import re
import sys


def compareTriplets(x, y):
    n = len(x)
    alex = 0
    bob = 0
    for i in range(n):
        if x[i] > y[i]:
            alex += 1
        elif x[i] < y[i]:
            bob += 1
        else:
            continue
    return [alex, bob]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    a = list(map(int, input().rstrip().split()))
    b = list(map(int, input().rstrip().split()))
    result = compareTriplets(a, b)
    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')
    fptr.close()
