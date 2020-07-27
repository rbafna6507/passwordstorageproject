import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)


list = ["username", "password"]
e_list = list.encode()
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)