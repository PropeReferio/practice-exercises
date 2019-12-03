def is_digit(n):
    import re
    x = re.findall('\d+', n)
    #print(x)
    y = re.findall('\D+', n)
    #print(y)
    return True if x and not y else False

#print(is_digit('234  '))

def validate_usr(username):
    import re
   # print(re.search('[0-9a-z\_]{4,16}', username))
    return True if re.findall('[0-9a-z\_]{4,16}', username) and not re.findall('[\s]', username) else False

#print(validate_usr('Hasd_12assssssasasasasasaasasasasas'))

import re
print(" ".join(re.split('[,;_\s]+', "A, very   very; irregular_sentence")))