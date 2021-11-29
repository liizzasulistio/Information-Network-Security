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

def encrypt_msg(message, hashed, private_key):
    # msg_hashed = hash_message(message)
    encrypted_message = ""

    # for i in msg_hashed:
    #     i = encrypt(ord(i), private_key)
    #     encrypted_message += str(i)
    # print(hashed)
    encrypted_hash = encrypt(hashed, private_key)
    # append_msg = message + "||" + str(encrypted_message)
    # append_msg = message.append("||") + encrypted_message
    # my_list = [str(message)]
    # print(encrypted_message)
    # my_list.append(encrypted_message)
    # append_msg = message.append(encrypted_message)

    # print(append_msg)
    # return append_msg
    # print(my_list)
    return message, encrypted_hash

def decrypt_msg(message, encrypted_hash, hashed, public_key):
    # message = ""
    checkValid = False

    # print(delivered_message)
    # message = encrypted_message.split("||")[0]
    # hashToBeCheck = encrypted_message.split("||")[1]
    # hashToBeCheck = hash_message(hashToBeCheck)
    # print(message)
    # print(hashToBeCheck)

    hashToBeCheck = encrypted_hash
    # print(hashToBeCheck)
    decrypt_hash = decrypt(hashToBeCheck, public_key)
    # print(decrypt_hash)

    if(hashed == decrypt_hash):
        checkValid = True

    return message, checkValid
    
def rsa_implementation(message, private_key, public_key):
    hashed = hash_message(message)
    message, encrypted_hash = encrypt_msg(message, hashed, private_key)
    print("Delivered: " + message)
    # decrypt_msg(message, encrypted_hash, hashed, public_key)
    decrypted_message, checkValid = decrypt_msg(message, encrypted_hash, hashed, public_key)
    print("Received: " + decrypted_message, checkValid)




if __name__ == '__main__':
    private_key, public_key = generate_keyPairs()
    message = "Hello World!"
    print("Message: " + message)
    print("Private Key: ",  private_key)
    print("Public Key: ", public_key)
    # hash_message(message)
    rsa_implementation(message, private_key, public_key)
    # delivered_msg = encrypt_msg(message, private_key)
    # received_msg, check = decrypt_msg(delivered_msg, public_key)
    # print("Delivered Message: " + delivered_msg)
    # print("Received Message: " + received_msg)
    # print("Check: " + str(check))

