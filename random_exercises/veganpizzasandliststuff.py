#Ex. 4-1 from Python Crash Course

pizzas = ["Cauli Cheez", "Soyrizo", "Margherita"]
your_pizzas = pizzas[:]
pizzas.append("Lentil Delight")
your_pizzas.append("Big Fat Sausage")

for pizza in pizzas:
    print(pizza + " is a vegan Italian delicacy.")
for pizza in your_pizzas:
    print(pizza + " lah lah I'm not vegan")
    
