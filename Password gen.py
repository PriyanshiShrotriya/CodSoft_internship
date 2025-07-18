import random
import string
def pass_generator(length):

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digit = string.digits
    symbol = "!@#$%&*_-^"
    all = lower + upper + digit + symbol
    password = ""
    
    for i in range(length):
        password += random.choice(all)
    return f" Your generated password : {password}"

length = int(input("Enter desired length: "))
print(pass_generator(length))
ch=input("Generate another Password ? (Yes/No)")
if ch =="yes" or ch == "YES":
    print(pass_generator(length))
else:
    pass
