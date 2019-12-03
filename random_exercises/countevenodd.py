odd = []
even = []

for x in range(1,10):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    
print(f"These are the even numbers: {even}")
print(f"These are the odd numbers: {odd}")