unit = input("Fahrenheit or Celsius?")
try_again = True

while try_again == True:

    if unit == "Fahrenheit":
        f = int(input("How many degrees Fahrenheit?"))
        c = f / 9 * 5 - 32 / 9 * 5
        print (f"{f} degrees Fahrenheit is {c} degrees Celsius.")
        try_again = False
    elif unit == "Celsius":
        c = int(input("How many degrees Celsius?"))
        f = c * 9 / 5 + 32
        print (f"{c} degrees Celsius is {f} degrees Fahrenheit.")
        try_again = False
    else:
        print ("What unit is that?")
        unit = input("Fahrenheit or Celsius?")