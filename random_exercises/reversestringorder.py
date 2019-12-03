# Exercise 15 from practicepython.org

def revstring(string):
    broken = string.split()
    length = len(broken)
    new = []
    while length > 0:
        new.append(broken[length - 1])
        length -= 1
    new = " ".join(new)
    return new

print(revstring(input("Give me a sentence, and I'll reverse the word order.")))