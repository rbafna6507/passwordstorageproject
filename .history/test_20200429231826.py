import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

key = Fernet.generate_key()

username = input("Username: ")
password = input("password: ")

e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)

e_userpass = [e_username, e_password]
outfile = open("test.pkl", "wb")
pickle.dump(passwords, outfile)
outfile.close()
infile = open('passwords.pkl','rb')
z = pickle.load(infile)
