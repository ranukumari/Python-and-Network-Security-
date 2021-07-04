'''1. Write a program in python to generate MD5 of string data'''

import hashlib #importing library

def main():  #defining main function

    password ="Ranu_Kumari@" #initializing string
    TextEncode = password.encode() #Text Encoding
    hash = hashlib.md5(TextEncode) #md5 hash function defined in hashlib library

    byte=hash.digest()  #returns encoded data in byte format
    hexa = hash.hexdigest() #returns encoded data in hexadecimal format

    print ("Equivalent Hexadecimal value of hash: ", hexa) #print the equivalent hexadecimal value
    print("Equivalent Byte vlaue of hash: ", byte)  #print the equivalent byte value

    return

main() #calling main function 