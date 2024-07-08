#!/bin/python3

import math
import os
import random
import re
import sys


def aVeryBigSum(arr):
    return sum(arr)


if __name__ == '__main__':
    ar_count = int(input().strip())
    ar = list(map(int, input().rstrip().split()))
    result = aVeryBigSum(ar)
