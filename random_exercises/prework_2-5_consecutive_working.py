check = [1,2,4,5]
check2 =[2,3,4,5,6,7]
total = 2
while total > 1:
    print("total = " + str(total))
    test = check.pop(0)
    print("test = " + str(test))
    print("check[0] = " + str(check[0]))
    total = len(check)
    """if test == a_list[0] - 1:
        return True
    else:
        return False
        total = 0"""


"""def is_consecutive(a_list):
    Checks to see if the numbers in a list are consecutive
    total = 2
    while total > 1:
        total = len(a_list)
        test = a_list.pop(0)
        if test == a_list[0] - 1:
            return True
        else:
            return False
            total = 0

works = is_consecutive(check)
print(works)"""