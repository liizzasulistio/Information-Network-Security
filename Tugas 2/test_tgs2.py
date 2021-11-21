import sdes
from sdes import *

def MAC(k, msg) :
    index = 0; flag = 0;
    current_text = ""

    for i in msg :
        if(flag == 0) :
            i = ord(i)
            i = encrypt(k, i)          

            flag = 1
            current_text = current_text + chr(i)
        
        else :
            i = ord(i) ^ ord(current_text[index-1])
            i = encrypt(k, i)

            current_text = current_text + chr(i)
        index = index + 1
    
    return current_text

def MAC_imp(k, msg) :
    encrypted = MAC(k, msg)

    return encrypted

def enkrip_message(k, m) :
    ciphertext2 = ""

    for i in m :
        i = encrypt(k, ord(i))
        ciphertext2 = ciphertext2 + chr(i)

    #enkrip = encrypt(k, ciphertext1)
    return ciphertext2

def dekrip_message(k, c) :
    plaintext2 = ""
    check = False

    for i in c :
        i = decrypt(k, ord(i))
        plaintext2 = plaintext2 + chr(i)

    before = plaintext2.split("||")[0]
    after = plaintext2.split("||")[1]

    h = MAC_imp(k, m)
    if(h == after) :
        check = True

    #enkrip = encrypt(k, ciphertext1)
    return before, check

def iec_imp(k, m) :
    h = MAC_imp(k, m)
    cipher_append_in = m + "||" + h

    cipher_internal = enkrip_message(k, cipher_append_in)
    plain_internal, hasil_check_internal = dekrip_message(k, cipher_internal)

    print("MAC Hash Only : ", h)
    print("Appended Hash : ", cipher_append_in)    
    print("Decrypt & Check Result : ", plain_internal, "-", hasil_check_internal)

if __name__ == "__main__" :
    k  = 0b1110101111
    m = "DEVIHAINUN"

    iec_imp(k, m)
    #MAC_imp(k, m)
