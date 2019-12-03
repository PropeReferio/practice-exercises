odd = []
even = []

for x in range(1,10):
    if x % 2 == 0:
        even.append(x)
    else:
        odd.append(x)
    
print(f"These are the even numbers: {even}. There are " len(even) "even numbers between 1 and 9.") 
print(f"These are the odd numbers: {odd}. There are " len(odd) "odd numbers between 1 and 9.") 

