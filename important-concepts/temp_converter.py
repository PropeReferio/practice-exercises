def convert_temp():

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

def cels_to_fahr(c):
    if type(c) not in [int, float]:
        raise TypeError("The input must be a number.")
    if c < -273.15:
        raise ValueError("The temperature cannot be less than absolute zero.")
    return c * 9 / 5 + 32

def fahr_to_cels(f):
    return f / 9 * 5 - 32 / 9 * 5

# testcases = [5,12, 34.0, True, -34, '34', [34,56]]

# for case in testcases:
#     print(cels_to_fahr(case), fahr_to_cels(case))