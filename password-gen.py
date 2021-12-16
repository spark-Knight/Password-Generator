import random 
import string

digits = list(string.digits)
alphabet = list(string.ascii_letters)

characters = digits + alphabet

def pasword_generator():
    # User will put length of password from length 

    length = int(input("enter password length: "))
    # It will shuffle characters

    random.shuffle(characters)
    # taking the random charactersfrom the password list

    password = []
    for i in range(length):
        password.append(random.choice(characters))

    # it will shufflethe result password
    random.shuffle(password)
    # converting into list to string
    # print password
    print("".join(password))