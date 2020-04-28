# This problem was asked by Microsoft.

# Given a dictionary of words and a string made up of those words (no spaces),
#  return the original sentence in a list. If there is more than one possible 
# reconstruction, return any of them. If there is no possible reconstruction, 
# then return null.

# For example, given the set of words 'quick', 'brown', 'the', 'fox', and the 
# string "thequickbrownfox", you should return ['the', 'quick', 'brown',
#  'fox'].

# Given the set of words 'bed', 'bath', 'bedbath', 'and', 'beyond', and the 
# string "bedbathandbeyond", return either ['bed', 'bath', 'and', 'beyond] or 
# ['bedbath', 'and', 'beyond'].

words = {'bed': 1,
         'bath': 1,
         'bedbath': 1,
         'and': 1,
         'beyond': 1}

s = 'bedbathandbeyond'

def buildSentence(words, s):
    final = []
    cur_i = 0
    active = True
    while active:
        cur_len = len(final)
        for k in words.keys():
            print('k:', k, '\nsubstring:', s[cur_i:len(k)+cur_i])
            if k == s[cur_i:len(k)+cur_i]:
                final.append(k)
                print('Adding key:', k)
                cur_i += len(k)
        if cur_len == len(final):
            active = False
    
    print('While loop ends, final is:', final)

    if ''.join(final) == s:
        return final

print(buildSentence(words, s))

#Use the length of each word in words to index the beginning of s and check
# for a match... i.e. if bed == s[:len('bed')]

#Then add that to a new list
#Keep track of indices
#check ''.join(final) against original, return if match, else None

