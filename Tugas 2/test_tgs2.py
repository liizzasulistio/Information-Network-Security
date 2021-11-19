import sdes
from sdes import *

def cbc_encrypt(k, plaintext) :
    #k  = 0b1110101111
    index = 0; flag = 0;
    current_text = ""

    #iv_bit = ord(iv)
    #k_bit = ord(k)

    for i in plaintext :
        if(flag == 0) :
            i = ord(i)
            i = encrypt(k, i)     # encrypt i with key
            i = i << 1            # geser 1 bit ke kiri (bitwise op)

            flag = 1
            current_text = current_text + chr(i)
        
        else :
            i = ord(i) ^ ord(plaintext[index-1])
            i = encrypt(k, i)
            i = i << 1

            current_text = current_text + chr(i)
        index = index + 1

    return current_text

def cbc_imp(k, plaintext) :
    encrypted = cbc_encrypt(k, plaintext)
    #decrypted = cbc_decrypt(k, iv, encrypted)
    return encrypted

def enkrip_message(k, m) :
    h = cbc_imp(k, m)

    ciphertext1 = m + "||" + h
    ciphertext2 = ""
    index = 0

    for i in ciphertext1 :
        i = ord(i)
        i = encrypt(k, i)     # encrypt i with key
        i = i << 1            # geser 1 bit ke kiri (bitwise op)

        ciphertext2 = ciphertext2 + chr(i)
        index = index + 1

    #enkrip = encrypt(k, ciphertext1)

    print(ciphertext1, " - ", ciphertext2)

if __name__ == "__main__" :
    k  = 0b1110101111
    m = "DEVIHAINUN"
    # k  = 0b1110101111
    iv = 0b0000000000
    enkrip_message(k, m)
