import sdes
import random
from sdes import *

# Implementasi Counter Mode
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

def main():
    plaintext = input("Masukkan plaintext: ")
    key = input("Masukkan key: ")
    k = ord(key)
    # k = 0b01100001

    print("Pilih counter IV yang diinginkan, 1 untuk memasukkan sendiri dan 2 untuk random")
    chose = int(input("Pilihan: "))
    if(chose == 1):
        ctr_iv = int(input("Masukkan counter IV: "))
        ctr_implementation(k, ctr_iv, plaintext)
    elif(chose == 2):
        ctr_iv = random.randrange(255)
        ctr_implementation(k, ctr_iv, plaintext)
    else:
        print("Pilihan tidak ada")

if __name__ == "__main__":
    main()