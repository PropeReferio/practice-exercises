def iq_test(numbers):
    new = numbers.split()
    print(new)
    even = []
    for x in new:
        even.append(int(x) % 2)
    print(even)
    if even.count(0) == 1:
        return (even.index(0) + 1)
    else:
        return (even.index(1) + 1)



print(iq_test("0 4 6 8 11"))