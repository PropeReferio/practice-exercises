#Ex. 4-1 from Python Crash Course

pizzas = ["Cauli Cheez", "Soyrizo", "Margherita"]
for pizza in pizzas:
    print(pizza + " is a vegan Italian delicacy.")

print("Pizza is pretty good.")    

cubes = [value**3 for value in range(1,15)]
millions = [value for value in range(1,1000001)]
print(max(millions))
print(min(millions))
print(sum(millions))
threes = [num for num in range(3,30,3)]
for num in threes:
    print(num)