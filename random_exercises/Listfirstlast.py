# Exercise 12 from practicepython.org

def randlist():
    import random
    a = []
    l = random.randint(11,20)  # Chooses a random length for list 'a'
    for x in range(1,l):
        a.append(random.randint(1,30))
    print(a)
    return a

a = randlist()

def firstlast(a):            # Adds the first and last elements from list a to list b
    b = []
    b.append(a[0])
    b.append(a[-1])
    print(b)

firstlast(a)