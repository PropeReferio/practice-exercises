import random

a = []
numbers = 10
while numbers > 0:                   # Makes a list of 10 integers between 1 and 99
  a.append(random.randint(1,100))
  numbers -= 1
b = []
print(f"A list of 10 numbers:{a}")

def evenlist(group):
  l = len(group)                     # Appends elements from above list to a new list
  while l > 0:
    if a[l-1] % 2 == 0:
      b.append(a[l-1])
    l -= 1
  print(f"Only the even numbers from that list:{b}")
  
evenlist(a)