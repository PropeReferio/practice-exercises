def duplicate_count(text):
    dup = 0
    s = 'abcdefghijklmnopqrstuvwxyz0123456789'
    for char in s:
        if text.count(char) > 1:
            dup += 1
    return dup

print(duplicate_count("indivisibility"))

print("indivisible".count("i"))
print(len(345))