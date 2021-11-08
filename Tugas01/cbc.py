import sdes
from sdes import *

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

            current_text = current_text + chr(i)
            flag = 1
        
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

            current_text = current_text + chr(i)
            flag = 1
        
        else :
            i = ord(i) >> 1
            i = decrypt(k_bit, i)
            i = i ^ ord(plaintext[index-1])

            current_text = current_text + chr(i)
        
        index = index + 1

    return current_text

def cbc(k, iv, plaintext) :
    for i in plaintext :
        encrypted = cbc_encrypt(k, iv, i)
        decrypted = cbc_decrypt(k, iv, encrypted)
        print(i, "-", encrypted, "-", decrypted)

if __name__ == "__main__" :
    cbc_key = 'f'
    iv = 'z'

    plaintext = input()
    print("--- CBC Result : ---")
    cbc(cbc_key, iv, plaintext)