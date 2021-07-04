'''3. Add salting and Iteration to hashes'''

import hashlib #importing library

def main():  #defining main function

    password ="Ranu_Kumari@" #initializing string
    salt="!123kum#$^"    #intializing salt
    db_password = password+salt   #Salting
    TextEncoding=db_password.encode() 

    '''Hash with MD5'''
    print("HASH WITH MD5")
    print("MD5: ",hashlib.md5(TextEncoding).hexdigest())

    '''Hash with SHA-2 (Secure Hash Algorithm 2): SHA2 is family of 4 hash functions i.e SHA-224, SHA-256, SHA-384 and SHA-512, SHA256 and SHA512 widely used'''
    print("\n")
    print("SHA2 HASH FUNCTION")
    print("SHA-224: ",hashlib.sha224(TextEncoding).hexdigest())  #sha224
    print("SHA-256: ",hashlib.sha256(TextEncoding).hexdigest())  #Sha256
    print("SHA-384: ",hashlib.sha384(TextEncoding).hexdigest())  #sha384
    print("SHA-512: ",hashlib.sha512(TextEncoding).hexdigest())  #sha512

    '''Hash with SHA-3 (Secure Hash Algorithm 3): SHA3 is family of 4 hash functions i.e SHA3-224, SHA3-256, SHA3-384 and SHA3-512'''
    print("\n")
    print("SHA3 HASH FUNCTION")
    print("SHA3-224: ",hashlib.sha3_224(TextEncoding).hexdigest())  #sha3_224
    print("SHA3-256: ",hashlib.sha3_256(TextEncoding).hexdigest())  #Sha3_256
    print("SHA3-384: ",hashlib.sha3_384(TextEncoding).hexdigest())  #sha3_384
    print("SHA3-512: ",hashlib.sha3_512(TextEncoding).hexdigest())  #sha3_512

    '''Hash with BLAKE2: BLAKE2 has hash function BLAKE2s and BLAKE2b'''
    print("\n")
    print("BLAKE2 HASH FUNCTION")
    print("BLAKE2s: ",hashlib.blake2s(TextEncoding).hexdigest())  #256-bit BLAKE2 or BLAKE2s
    print("BLAKE2b: ",hashlib.blake2b(TextEncoding).hexdigest())  #512-bit BLAKE2 or BLAKE2b

    return

main() #calling main function 