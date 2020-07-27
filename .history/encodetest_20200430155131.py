import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)

key = Fernet.generate_key()
list = ["username", "password"]
en_list = bytes(list)
e_list = encrypt(en_list, key)