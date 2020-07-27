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
e_userpass = {"Youtube.com" : ["Username: " + str(e_username), "Password: " + str(e_password)]}
outfile = open("test.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('test.pkl','rb')
z = pickle.load(infile)
print(z)
e_userpass = z
for key in e_userpass:
    for i in list:
        decrypt(i, key)