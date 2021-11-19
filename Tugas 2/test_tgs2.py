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
    print(encrypted)

    return encrypted

def enkrip_message(k, m) :
    ciphertext2 = ""
    index = 0

    for i in m :
        i = encrypt(k, ord(i))
        #i = i << 1

        ciphertext2 = ciphertext2 + chr(i)
        index = index + 1

    #enkrip = encrypt(k, ciphertext1)
    return ciphertext2

def dekrip_message(k, c) :
    plaintext2 = ""
    index = 0

    for i in c :
        #i = ord(i) >> 1
        i = decrypt(k, ord(i))

        plaintext2 = plaintext2 + chr(i)
        index = index + 1

    #enkrip = encrypt(k, ciphertext1)

    return plaintext2

def iec_imp(k, m) :
    h = cbc_imp(k, m)
    ciphertext1 = m + "||" + h

    cipher = enkrip_message(k, ciphertext1)
    plain = dekrip_message(k, cipher)
    print(ciphertext1, "-", cipher, "-", plain)

if __name__ == "__main__" :
    k  = 0b1110101111
    m = "DEVIHAINUN"
    # k  = 0b1110101111
    iv = 0b0000000000
    #iec_imp(k, m)
    cbc_imp(k, m)

