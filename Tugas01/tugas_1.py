import sdes
import random
from sdes import *

# -------------------------- 3DES 2 KEY ----------------------
def encrypt_3DES_2key(key1, key2, plaintext):
    a = encrypt(ord(key1), ord(plaintext))
    b = decrypt(ord(key2), a)
    c = encrypt(ord(key1), b)    
    current_text = chr(c)
    return current_text

def decrypt_3DES_2key(key1, key2, ciphertext):
    a = decrypt(ord(key1), ord(ciphertext))
    b = encrypt(ord(key2), a)
    c = decrypt(ord(key1), b)    
    current_text = chr(c)
    return current_text

def tripleDES2key(key1, key2, plaintext):
    for i in plaintext:
      a = encrypt_3DES_2key(key1, key2, i)
      b = decrypt_3DES_2key(key1, key2, a)
      #print(i, "-", a, "-", b)
      print(i, "-", b)

# -------------------------- 3DES 3 KEY -----------------------
def encrypt_3DES_3key(key1, key2, key3, plaintext):
    a = encrypt(ord(key1), ord(plaintext))
    b = decrypt(ord(key2), a)
    c = encrypt(ord(key3), b)    
    
    current_text = chr(c)
    return current_text

def decrypt_3DES_3key(key1, key2, key3, plaintext):
    a = decrypt(ord(key3), ord(plaintext))
    b = encrypt(ord(key2), a)
    c = decrypt(ord(key1), b)    
    
    current_text = chr(c)
    return current_text

def tripleDES3key(key1, key2, key3, plaintext):
    for i in plaintext:
      a = encrypt_3DES_3key(key1, key2, key3, i)
      b = decrypt_3DES_3key(key1, key2, key3, a)
      #print(i, "-", a, "-", b)
      print(i, "-", b)

# -------------------------- CBC -----------------------------
def cbc_encrypt(k, iv, plaintext) :
    index = 0; flag = 0;
    current_text = ""

    iv_bit = ord(iv)
    k_bit = ord(k)

    for i in plaintext :
        if(flag == 0) :
            i = ord(i) ^ iv_bit         # XOR operation
            i = encrypt(k_bit, i)       # encrypt i with key
            i = i << 1                  # geser 1 bit ke kiri (bitwise op)

            flag = 1
            current_text = current_text + chr(i)
        
        else :
            i = ord(i) ^ ord(plaintext[index-1])
            i = encrypt(k_bit, i)
            i = i << 1

            current_text = current_text + chr(i)
        index = index + 1

    return current_text

def cbc_decrypt(k, iv, ciphertext) :
    index = 0; flag = 0;
    current_text = ""

    iv_bit = ord(iv)
    k_bit = ord(k)

    for i in ciphertext :
        if(flag == 0) :
            i = ord(i) >> 1             # XOR operation
            i = decrypt(k_bit, i)       # encrypt i with key
            i = i ^ iv_bit              # geser 1 bit ke kiri (bitwise op)

            flag = 1
            current_text = current_text + chr(i)
        
        else :
            i = ord(i) >> 1
            i = decrypt(k_bit, i)
            i = i ^ ord(plaintext[index-1])

            current_text = current_text + chr(i)
        index = index + 1

    return current_text

# ------------------------- CTR ---------------------------
def ctr_encrypt(k, ctr_iv, plaintext):
    ciphertext = ""
    for i in range(0, len(plaintext)):
        ctr_enc = encrypt(k, ctr_iv)
        i = ord(plaintext[i]) ^ ctr_enc
        ctr_iv += 1
        ctr_iv %= 256
        ciphertext += chr(i)
    return ciphertext

def ctr_decrypt(k, ctr_iv, ciphertext):
    plaintext = ""
    for i in range(0, len(ciphertext)):
        ctr_dec = encrypt(k, ctr_iv)
        i = ord(ciphertext[i]) ^ ctr_dec
        ctr_iv += 1
        ctr_iv %= 256
        plaintext += chr(i)
    return plaintext

def ctr_implementation(k, ctr_iv, plaintext):
    encryption = ctr_encrypt(k, ctr_iv, plaintext)
    decryption = ctr_decrypt(k, ctr_iv, encryption)
    print(plaintext, '-', encryption, '-', decryption)

def cbc_imp(k, iv, plaintext) :
    encrypted = cbc_encrypt(k, iv, plaintext)
    decrypted = cbc_decrypt(k, iv, encrypted)
    print(plaintext, "-", encrypted, "-", decrypted)

if __name__ == "__main__" :
    key1 = "h"
    key2 = "y"
    key3 = "s"

    cbc_key = "f"
    cbc_iv = "z"

    plaintext = input("Masukkan plaintext: ")
    key = "k"
    ctr_key = ord(key)

    print("Pilih counter IV yang diinginkan, 1 untuk memasukkan sendiri dan 2 untuk random")
    chose = int(input("Pilihan: "))
    if(chose == 1):
        ctr_iv = int(input("Masukkan counter IV: "))
    elif(chose == 2):
        ctr_iv = random.randrange(255)
    else:
        print("Pilihan tidak ada")

    print("--- Hasil 3DES 2 KEY : ---")
    tripleDES2key(key1, key2, plaintext)
    print("--- Hasil 3DES 3 KEY : ---")
    tripleDES3key(key1, key2, key3, plaintext)
    print("--- Hasil CBC : ---")
    cbc_imp(cbc_key, cbc_iv, plaintext)
    print("--- Hasil CTR : ---")
    ctr_implementation(ctr_key, ctr_iv, plaintext)
