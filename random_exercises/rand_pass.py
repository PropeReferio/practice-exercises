# Ex 16 from practicepython.org Write a password generator in Python. Be 
#creative with how you generate passwords - strong passwords have a mix 
# of lowercase letters, uppercase letters, numbers, and symbols. The 
# passwords should be random, generating a new password every time the 
# user asks for a new password. Include your run-time code in a main method.


def generate_password(s):
    import random
    pass_length = random.randint(8,20)
    password = ""
    while pass_length > 0:
        new_char = s[random.randint(0, len(s) - 1)]
        password += new_char
        pass_length -= 1
    return password

s = "abcdefghijklmnopqrstuvwxyz0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"

print(generate_password(s))