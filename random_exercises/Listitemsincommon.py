import random
def randlist(length,group):
  while length > 0:
    length -= 1
    group.append(random.randint(1,20))

a = []
b = []
c = []

randlist(random.randint(10,21),a)                     # Generates two random lists, and appends to a third list the elements they have in common
randlist(random.randint(10,21),b)
print(f"A list: {a}")
print(f"B list: {b}")

for x in range(1000):
  if x in a and x in b:
    c.append(x)
    
print(f"C list: {c}")