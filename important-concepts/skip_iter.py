s = 'happy birthday!'

for i in range(len(s)):
    if s[i] == 'y':
        i += 10
    else:
        print(s[i])
