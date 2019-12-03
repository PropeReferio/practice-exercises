#Exercise 11 from practicepython.org

def primecheck(num):
    p=[]
    while num > 0:
        for x in range(1,num+1):
            if num % x == 0:
                p.append(x)
        if len(p) == 2:
            print(f"{num} is prime.")
        else:
            print(f"{num} is not prime. It's divisors are {p}.")
        num -= 1
        p = []



primecheck(int(input("Give me a number and I'll check if it's prime, and every number less than it!")))