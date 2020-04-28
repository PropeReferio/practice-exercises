def dirReduc(arr):
#Step 2: Wrap this in a while loop, while count = 0
#where count increments each time an adjacent opposite is found
#Step 1: Loop through arr[:], checking for adjacent opposites 
#and deleting them from arr
    new_list = arr.copy()
    active = True
    while active:
        checklength = len(arr)
        for i, way in enumerate(new_list[0:-1]):
            print(i, way)
            if way == 'NORTH' and new_list[i+1] == 'SOUTH' or way == \
    'SOUTH' and new_list[i+1] == 'NORTH' or way == 'WEST' and \
    new_list[i+1] == 'EAST' or way == 'EAST' and new_list[i+1] == 'WEST':
                del arr[i:i+2]
        if checklength != len(arr):
            active = False
    return arr
    