import sdes
import random
from sdes import *

# key bebas 10 bit
# inputnya 8 bit (1 char)

def encrypt_3DES_2key(key1, key2, plaintext):
    """Encrypt plaintext with given key"""
    a = encrypt(ord(key1), ord(plaintext))
    b = decrypt(ord(key2), a)
    c = encrypt(ord(key1), b)    
    current_text = chr(c)
    return current_text


def decrypt_3DES_2key(key1, key2, ciphertext):
    """Decrypt ciphertext with given key"""
    a = decrypt(ord(key1), ord(ciphertext))
    b = encrypt(ord(key2), a)
    c = decrypt(ord(key1), b)    
    current_text = chr(c)
    return current_text

def tripleDES2key(key1, key2, plaintext):
    print("-----tripleDES2key-----")
    for i in plaintext:
      a = encrypt_3DES_2key(key1, key2, i)
      b = decrypt_3DES_2key(key1, key2, a)
      print(i, " - ", b)
# ---------------------------------------------------------
def encrypt_3DES_3key(key1, key2, key3, plaintext):
    """Encrypt plaintext with given key"""
    a = encrypt(ord(key1), ord(plaintext))
    b = decrypt(ord(key2), a)
    c = encrypt(ord(key3), b)    
    
    current_text = chr(c)
    return current_text

def decrypt_3DES_3key(key1, key2, key3, plaintext):
    """Decrypt ciphertext with given key"""
    a = decrypt(ord(key3), ord(plaintext))
    b = encrypt(ord(key2), a)
    c = decrypt(ord(key1), b)    
    
    current_text = chr(c)
    return current_text

def tripleDES3key(key1, key2, key3, plaintext):
    print("-----tripleDES3key-----")
    for i in plaintext:
      a = encrypt_3DES_3key(key1, key2, key3, i)
      b = decrypt_3DES_3key(key1, key2, key3, a)
      print(i, " - ", b)
# ------------------------------------------------------------

if __name__ == '__main__':
    plaintext = input("Masukkan kata apapun: ")
    key1 = "h"
    key2 = "y"
    key3 = "c"
    tripleDES2key(key1, key2, plaintext)
    tripleDES3key(key1, key2, key3, plaintext)
