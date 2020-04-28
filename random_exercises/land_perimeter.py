def land_perimeter(arr):
    #["OXOOOX",
    # "OXOXOO", 
    # "XXOOOX", 
    # "OXXXOO", 
    # "OOXOOX", 
    # "OXOOOO", 
    # "OOXOOX", 
    # "OOXOOO", 
    # "OXOOOO", 
    # "OXOOXX"]
    #Use modulo to stay within bounds of map.
    xlen = len(arr[0])
    ylen = len(arr)
    print('This map is {} squares wide and {} squares deep.'.format(xlen,ylen))
    perim = 0
    for row in arr:
        for spot in row:
            if spot == "X":
                xperim = 4 # Subtract 1 for every adjacent x, then add to total perimeter
                xcoor = row.index(spot)
                ycoor = arr.index(row)
                print(xcoor,ycoor)
                
    #return #perimeter of all the islands
    
    
 