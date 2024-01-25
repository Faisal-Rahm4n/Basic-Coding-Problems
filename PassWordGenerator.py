import string
import random

def gen():
        s1 = string.ascii_uppercase

        s2 = string.ascii_lowercase

        s4 = string.digits

        s3 = string.punctuation

        passlen = int(input("Enter The Password length\n"))

        s=[]
        s.extend(list(s1))
        s.extend(list(s2))
        s.extend(list(s3))
        s.extend(list(s4))


        random.shuffle(s)

        pas = ("".join(s[0:passlen]))
        print(pas)

gen()