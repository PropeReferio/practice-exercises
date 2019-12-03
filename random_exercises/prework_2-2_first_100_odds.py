#Print first 100 odd numbers in Python.

odds = []
for x in range(1,200):
    if x % 2 != 0:
        odds.append(x)

for x in odds:
    print(x)

print("You printed " + str(len(odds)) + " numbers.")