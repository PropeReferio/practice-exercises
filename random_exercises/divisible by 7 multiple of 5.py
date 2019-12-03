
def divisiblelist(min, max):
    divisible_list=[]
    for x in range (min, max):
        if x % 7 == 0:
            if x % 5 == 0:
                divisible_list.append(x)
    print (divisible_list)

divisiblelist(1500,2701)
