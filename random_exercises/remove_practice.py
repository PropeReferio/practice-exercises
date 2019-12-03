def gimme(arr):
    new = arr[:]
    new.remove(min(new))
    print(new)
    
gimme([1,5,10])