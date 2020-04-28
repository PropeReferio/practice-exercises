def multiple_of_index(arr):
    print(arr)
    for i, x in enumerate(arr):
        print(i,x)
    def divisible_by_index(lst):
        for i, x in enumerate(lst):
            if not x % i:
                return True
            else:
                return False
    #return list(filter(divisible_by_index, arr[1:]))
    #The problem is that filter wants to run my function on each item of arr[:1], but those can't be enumerated.
    #use enumerate
    #my_enumerate = lambda x :[(t, x[t]) for t in range(len(x))]