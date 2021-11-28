import rsa_python
from rsa_python import *
import hashlib


# Alice mengirim Message
# Message -> 

def hash_message(message):
    m = hashlib.sha3_256()
    m.update(message.encode('utf-8'))
    hashed_m = ""
    for i in m.digest():
        hashed_m += str(hex(i))
    # print(hashed_m)
    return hashed_m

def encrypt_msg(message, private_key):
    msg_hashed = hash_message(message)
    encrypted_message = ""

    for i in msg_hashed:
        i = encrypt(ord(i), private_key)
        encrypted_message += str(i)
    print(encrypted_message)






if __name__ == '__main__':
    private_key, public_key = generate_keyPairs()
    message = "Hello World!"
    print("Message: " + message)
    print("Private Key: ",  private_key)
    print("Public Key: ", public_key)
    # hash_message(message)
    encrypt(message, private_key)
