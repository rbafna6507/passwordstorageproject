import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)


list = ["username", "password"]
en_list = list.encode()
