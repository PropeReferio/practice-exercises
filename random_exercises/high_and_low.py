def high_and_low(numbers):
    num_list = numbers.split(" ")
    num_list = list(map(int, num_list))
    print(num_list)
    return str(max(num_list)) + " " + str(min(num_list))

print(high_and_low("4 5 29 54 4 0 -214 542 -64 1 -3 6 -6"))