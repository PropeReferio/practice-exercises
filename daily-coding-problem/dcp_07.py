# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count 
# the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 
# 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not 
# allowed.

#Questions for interviewer: Will the input always be a string of digits,
#or sometimes other datatypes like floats, ints, lists?

def is_valid(substring):
    if substring[0] == '0':
        return False
# ord('a') - 96 = 1
def count_the_ways(code):
    '''Takes a coded numerical message and counts the possible decoded
    messages. '''
    # First drop all zeros. They can only be preceded by 1 or 2, and only
    # decoded in one way.
    #This doesn't work, because then a 2 or 1 can be adjacent to another
    #Number it wasn't previously pairable with.
    nozeros = ''
    dont_check = []
    for i, char in enumerate(code[::-1]):
        if char == '0':
            dont_check.append(i+1)
        elif i in dont_check:
            continue
        else:
            nozeros += char
    nozeros = nozeros[::-1]
    print(nozeros)

    ways = 1
    #For each 1 or 2 followed by a number <= 6, increment ways by 1


#Look at each pair of chars. If <= 26, and the chars after it won't cause an error
# i.e. '21054', then that pair can be decoded as a single letter.

count_the_ways('21054418395726154')


    

#Write a helper function to see if substring after a valid pair would also
#be valid. If so, you can decode the pair.
