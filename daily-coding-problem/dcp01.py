# This problem was recently asked by Google.
#
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.

def find_sum(lst, value):
    for idx, val in enumerate(lst):
        if (value - val) in lst[idx+1:]:
            return True
    return False

print(find_sum([10,15,3,7], 17))
print(find_sum([5, -5,3,7], 10))
print(find_sum([5, -5,3,8], 10))