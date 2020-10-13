import random
import string

def generate():

    s1 = string.ascii_uppercase
    s2 = string.ascii_lowercase
    s3 = string.digits
    s4 = string.punctuation

    passLen = int(input("Enter the length of password which you want to set: "))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s) # shuffling s

    password = ("".join(s[0:passLen]))
    print(password)


generate()