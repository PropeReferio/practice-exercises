def expanded_form(num):
    x = str(num)
    y = x.rstrip('0')
    n = ''
    i = 1 # index + 1
    length = len(x)
    print(length)
    for char in x:
        if int(char) > 0:
            n += char
            while length - i > 0:    #Adds a number of zeros based on index in the string
                n += '0'
                length -= 1
            length = len(x)
            x[i:]
            if length - i > 0: #.find tries to check if the rest of string is only zeros.
                n += ' + '
        i += 1
    return n

print(expanded_form(7030400))

