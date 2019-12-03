def remove_smallest(numbers):
    if numbers:
        numbers[:].remove(min(numbers))
    x = numbers[:]
    return x

print(remove_smallest([1, 2, 3, 4, 5]))