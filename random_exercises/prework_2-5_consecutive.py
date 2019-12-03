#Write a function to check to see if all numbers in list are consecutive
#numbers. For example, [2,3,4,5,6,7] are consecutive numbers, but [1,2,4,5]
#are not consecutive numbers. The return should be boolean Type.

check = [1,2,4,6]
check2 =[2,3,4,5,6,7]

def is_consecutive(a_list):
    """Checks to see if the numbers in a list are consecutive"""
    total = 2
    while total > 1:
        test = a_list.pop(0)
        if test == a_list[0] - 1:
            total = len(a_list)
        else:
            return False
            break
    return True

works = is_consecutive(check)
print(works)
