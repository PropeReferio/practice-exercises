def find_next_square(sq):
    x = sq ** 0.5
    return int((x + 1) ** 2) if x.is_integer() else -1

print(find_next_square(169))

print(5.2%1)