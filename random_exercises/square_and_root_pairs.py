#Are they the same? kata on codewars.com

def comp(a1, a2):
    if not a1 or not a2:
        return False
    for num in a1:
        if num ** 2 not in a2:
            return False
        else:
            a1.remove(num)
            a2.remove(num ** 2)
            print(a1)
            print(a2)
    for num in a2:
        if num ** 0.5 not in a1:
            return False
        else:
            a2.remove(num)
            a1.remove(num ** 0.5)
    return True
    #So [2,2,3] and [4,4,9] works fine, but [2,2,3] and [4,9,9] doesn't work 
    #since for the second 9 there isn't a second 3.