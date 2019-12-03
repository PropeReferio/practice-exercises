def getCount(inputStr):
    count = 0
    for let in inputStr:
        if let in "aeiou":
            count += 1
    return count
                
def getCount(inputStr):
    return sum(1 for let in inputStr if let in "aeiouAEIOU")