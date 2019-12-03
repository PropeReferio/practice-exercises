# Exercise 14 from practicepython.org

import random
def randlist(length,group):
  while length > 0:
    length -= 1
    group.append(random.randint(1,11))
  print(group)
  return group

a = []

def cleanlist(a):
    a = set(a)
    print(a)

a = randlist(random.randint(20,31),a)
cleanlist(a)