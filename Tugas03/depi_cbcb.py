'''
Created on 07.09.2016

@author: Marius

url : https://raw.githubusercontent.com/mx0c/RSA-Implementation-in-Python/master/main.py
'''

import random
import hashlib
max_PrimLength = 1000000000000

'''
calculates the modular inverse from e and phi
'''
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

'''
calculates the gcd of two ints
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
checks if a number is a prime
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generateRandomPrim():
    while(1):
        ranPrime = random.randint(0,max_PrimLength)
        if is_prime(ranPrime):
            return ranPrime

def generate_keyPairs():
    p = generateRandomPrim()
    q = generateRandomPrim()
    
    n = p*q
    print("n ",n)
    '''phi(n) = phi(p)*phi(q)'''
    phi = (p-1) * (q-1) 
    print("phi ",phi)
    
    '''choose e coprime to n and 1 > e > phi'''    
    e = random.randint(1, phi)
    g = gcd(e,phi)
    while g != 1:
        e = random.randint(1, phi)
        g = gcd(e, phi)
        
    print("e=",e," ","phi=",phi)
    '''d[1] = modular inverse of e and phi'''
    d = egcd(e, phi)[1]
    
    '''make sure d is positive'''
    d = d % phi
    if(d < 0):
        d += phi
        
    #print("KEYS: ", ((e,n),(d,n)))
    return ((e,n),(d,n))
        
def decrypt(ctext,private_key):
    try:
        key,n = private_key
        text = [chr(pow(char,key,n)) for char in ctext]
        return "".join(text)
    except TypeError as e:
        print(e)

def encrypt(text,public_key):
    key,n = public_key
    ctext = [pow(ord(char),key,n) for char in text]
    return ctext

# ---------------------------------------- TUGAS ------------------------------------------

def hash_message(message) :
    m = hashlib.sha256()
    m.update(message.encode('utf-8'))

    hashed_msg = ""

    for i in m.digest() :
        hashed_msg = hashed_msg + str(hex(i))

    #print(hashed_msg)
    return hashed_msg

def encrypt_out(message, private_key) :
    ciphertext2 = []
    ciphertext2 = encrypt(message, private_key)
    
    return ciphertext2

def decrypt_out(cipher, public_key) :
    plaintext2 = []
    plaintext2 = decrypt(cipher, public_key)

    return plaintext2

def rsa_imp(private_key, public_key, m) :
    checker = False

    hashed1 = hash_message(m)
    print("---------------- HASH ONLY -----------------")
    print(hashed1, "\n")
    encrypted_hash = encrypt_out(hashed1, private_key)

    hash_pad = bytes("||", encoding='UTF-8')
    hash_append = [m, hash_pad, encrypted_hash]
    print("-------------- APPENDED HASH ---------------")
    print(hash_append, "\n")

    original_message = hash_append[0]
    encrypted = hash_append[2]

    hashed2 = hash_message(original_message)
    decrypted_hash = decrypt_out(encrypted, public_key)

    print("------------- DECRYPTED HASH ---------------")
    print(decrypted_hash, "\n")


    if(hashed2 == decrypted_hash) :
        checker = True
    print("Hasil Cek : ", checker)

if __name__ == '__main__':
    public_key,private_key = generate_keyPairs() 
    print("Public Key : ",public_key)
    print("Private Key : ",private_key)
 
    public_key, private_key = generate_keyPairs()
    message = "Hello World" 

    rsa_imp(private_key, public_key, message)
