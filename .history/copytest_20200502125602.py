import pickle
import cryptography
from cryptography.fernet import Fernet

"""def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)
"""

infile = open('jeff.pkl','rb')
z = pickle.load(infile)
key = Fernet.generate_key()
e_userpass = z
username = input(b"Username: ")
password = input(b"password: ")
website = input("Website: ")
e_username = encrypt(username)
e_password = encrypt(password)
e_list = [b"Username: " + e_username, b"Password: " + e_password]
e_userpass["Website: " + website] = e_list
outfile = open("jeff.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('jeff.pkl','rb')
z = pickle.load(infile)
e_userpass = z
j = [e_userpass[k] for k in e_userpass]
for k in j:
    for q in k:
        decrypt(q)

"""for key, value in d_userpass.items():
    print(key, ' : ', value)"""