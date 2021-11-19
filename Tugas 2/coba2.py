import sdes
from sdes import *

def MAC(K, MSG):
    k  = 0b1110101111
    index = 0; flag = 0;
    current_text = ""

    for i in MSG :
        if(flag == 0) :
            i = ord(i)
            i = encrypt(k, i)     # encrypt i with key
            i = i << 1            # geser 1 bit ke kiri (bitwise op)

            flag = 1
            current_text = current_text + chr(i)
        
        else :
            i = ord(i) ^ ord(MSG[index-1])
            i = encrypt(k, i)
            i = i << 1

            current_text = current_text + chr(i)
        index = index + 1

    return current_text


def internal_encrypt(K, M):
    cipertext = []
    # mac = MAC(k, m)
    for i in M:
        cipertext.append(i)
    print(cipertext)

if __name__ == "__main__" :
    k  = 0b1110101111
    m = "DEVIHAINUN"
    # k  = 0b1110101111
    iv = 0b0000000000
    mac = MAC(k, m)
    internal_encrypt(k, mac)