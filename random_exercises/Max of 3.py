#Excercise 28 from practicepython.org

def maxthree():

    var1 = int(input("Give me a number!"))
    var2 = int(input("And a second!"))
    var3 = int(input("And a third!"))

    if var1 > var2 and var1 > var3:
        print(f"The first number is the biggest. It is {var1}.")
    elif var2 > var1 and var2 > var3:
        print(f"The second number is the biggest. It is {var2}.")
    elif var3 > var1 and var3 > var2:
        print(f"The third number is the biggest. It is {var3}.")
    else:
        print("The two biggest numbers are the same.")

maxthree()
