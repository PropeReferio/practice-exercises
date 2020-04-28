#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'mergeArrays' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

a = [1, 2, 3]
            #   ^
b = [2, 5, 5]
            #   ^
op = [1, 2, 2, 3, 5, 5]

# O(n), n=len(a)+len)b

# https://stackoverflow.com/questions/14236172/built-in-sort-method-of-python

"""
Comm:
- asking clariffying questions, [], None, 
- can the arrays be of unequal lengths?

Problem Solving:

- come up with the optimal approach to solve the problem/ discuss differnet approach, talk about their tradeoffs, and pick one to code out.
- Brush up on time/space complexities

Coding:
- being prof in lang of choice

Verification:
- proactively check for bugs and edge cases

"""

#O(len(a)+len(b)) ~ O(n)
def mergeArrays(a, b):

    # return sorted(a+b)
    
    a_idx = 0
    b_idx = 0
    c = []
    
    # 0<3 -> O(1)
    
    # [1,2,3]

    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            c.append(a[a_idx])
            a_idx += 1
        else:
            c.append(b[b_idx])
            b_idx += 1
    if a_idx == len(a):
        c.extend(b[b_idx:])
    else:
        c.extend(a[a_idx:])
    return c

# a = []
# b = [1,2,3]
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a_count = int(input().strip())

    a = []

    for _ in range(a_count):
        a_item = int(input().strip())
        a.append(a_item)

    b_count = int(input().strip())

    b = []

    for _ in range(b_count):
        b_item = int(input().strip())
        b.append(b_item)

    result = mergeArrays(a, b)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
