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
    # print("Encrypt : ", cipher_internal)    # buat check aja
    print("Decrypt & Check Result : ", plain_internal, "-", hasil_check_internal)


def encrypt_message_ext(k, m):
    ciphertext_ext = ""

    # Melakukan enkripsi pada message yang akan dikirimkan
    for i in m:
        i = encrypt(k, ord(i)) # enkripsi dengan library sdes
        ciphertext_ext = ciphertext_ext + chr(i)

    # Menambahkan MAC hash pada message yang akan dikirimkan
    cipher_append_ext = ciphertext_ext + "||" + MAC_imp(k, m)
    return cipher_append_ext

def decrypt_message_ext(k, m, check):
    a = "" # plaintext
    checkValid = False # check validasi
    FM = "" # MAC hash yang dibawa oleh message
    
    # Melakukan pemisahan pada message yg telah dikirimkan
    message = m.split("||")[0]
    FM = m.split("||")[1]

    # cek apakah MAC asli sama dengan yang dibawa oleh message
    if(check == FM):
        checkValid = True

    # Dekripsi message yang dikirimkan
    for i in message:
        i = decrypt(k, ord(i)) # dekripsi dengan library sdes
        a += chr(i)

    return a, checkValid

def cipher_ext(k, m):
    check = MAC_imp(k, m)

    encrypt_external = encrypt_message_ext(k, m)
    decrypt_external, checkFM = decrypt_message_ext(k, encrypt_external, check)
    print("Ciphertext External : ", encrypt_external)
    print("Decrypt External : ", decrypt_external, '-', checkFM)

if __name__ == "__main__" :
    k  = 0b1110101111
    m = "DEVIHAINUN"

    iec_imp(k, m)
    cipher_ext(k, m)
    #MAC_imp(k, m)
