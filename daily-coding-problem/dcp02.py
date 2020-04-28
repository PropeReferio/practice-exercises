# This problem was asked by Uber.

# Given an array of integers, return a new array such that each element at 
# index i of the new array is the product of all the numbers in the original 
# array except the one at i.

# For example, if our input was [1, 2, 3, 4, 5], the expected output would be 
# [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would
#  be [2, 3, 6].

# Follow-up: what if you can't use division?

lst = [1, 2, 3, 4, 5]
# lst = [3,2,1]

def product_divided(lst):
    product = 1
    for x in lst: #Linear time
        product *= x
    return list(map(lambda x: product // x, lst)) #Linear time 

print(product_divided(lst))


def multiply_els(lst):
    newlst = []
    for i in range(len(lst)):
        base = 1
        for j in range(len(lst)): #Nested for loops, quadratic time.
            if j == i:
                continue
            base *= lst[j]
        newlst.append(base)
    return newlst


final = multiply_els(lst)
print(final)