
def iq_test(numbers):
    even = []
    for x in numbers:
        even.append(x % 2)
    while 0 in even[:]:
        even[:].remove(0)
    if len(even[:]) == 1:
        return (even.index(1) + 1)
    else:
        return (even.index(0) + 1)



print(iq_test([0, 4, 6, 8, 11]))