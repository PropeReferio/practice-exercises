# This problem was asked by Stripe.

# Given an array of integers, find the first missing positive integer in linear time and constant 
# space. In other words, find the lowest positive integer that does not exist in the array. 
# The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

# You can modify the input array in-place.

arr = [3,4,-1,1]

arr = [-5, -2, 1,2,3,4,5,6,7,8,9]

def find_lowest_int(lst):
    no_negs = list(filter(lambda x: x >= 1, lst)) # O(n)
    print(no_negs)
    for x in range(1, max(lst)+2):
        if x not in no_negs:  #O(n**2)
            return x
    return -1

print(find_lowest_int(arr))

# Maybe merge sort the array, omitting values < 1.   n log n
# Then, check that each item in the list increments by 1. If it doesn't, you've found the lowest missing positive integer.

def merge(a,b):
    a_idx, b_idx, c = 0, 0, []
    while a_idx < len(a) and b_idx < len(b):
        if a[a_idx] < b[b_idx]:
            if a[a_idx] >= 1:
                c.append(a[a_idx])
            a_idx += 1
        else:
            if b[b_idx] >= 1:
                c.append(b[b_idx])
            b_idx += 1
    if a_idx < len(a):
        c.extend(a[a_idx:])
    else:
        c.extend(b[b_idx:])
    return c

def merge_sort(lst):
    if len(lst) <= 1: return lst
    left, right = merge_sort(lst[:len(lst)//2]), merge_sort(lst[len(lst)//2:])
    return merge(left, right)

print(merge_sort([50, -32, 21, -5, 8, 9, 136, 2]))

def find_low_int(lst):
    srted = merge_sort(lst)   # O(n * log(n))
    for i, num in enumerate(srted):    #O(n)
        if i + 1 != num:  #O(1)
            return i + 1  #O(1)
    
print(find_low_int([50, -32, 21, -5, 8, 9, 136, 2, 1]))