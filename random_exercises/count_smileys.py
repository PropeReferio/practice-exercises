#Count the smiley faces! from codewars.com

def count_smileys(arr):
    count = 0
    for smile in arr:
        eye = False
        nose = False
        mouth = False
        if len(smile) == 2:
            if smile[0] == ":" or ";":
                eye = True
            else:
                continue
            if smile[1] == ")" or "D":
                mouth = True
            else:
                continue
            if eye and mouth:
                count += 1
        if len(smile) == 3:
            if smile[0] == ":" or ";":
                eye = True
            else:
                continue
            if smile[1] == "-" or "~":
                nose = True
            else:
                continue
            if smile[2] == ")" or "D":
                mouth = True
            else:
                continue
            if eye and nose and mouth:
                count += 1
    return count

print(count_smileys([';]', ':[', ';*', ':$', ';-D']))
console.log