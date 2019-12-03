def factorial(number):
    x = 1
    while number > 0:
        x *= number
        number = number - 1
    return x
n = int(input("Give me a number, and I'll compute the factorial!"))
print(factorial(n))
