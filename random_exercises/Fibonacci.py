#Exercise #13 from practicepython.org

def fib(num):
    f = 1
    flist = []
    count = num
    while num > 0:
        flist.append(f)
        f = flist[count-num] + flist[count-num-1]
        num -= 1
    print(flist)

fib(int(input("How many fibonacci numbers would you like?")))