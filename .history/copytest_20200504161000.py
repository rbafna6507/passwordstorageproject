import pickle
import cryptography
from cryptography.fernet import Fernet

"""def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)
"""
e_userpass = {}
key_infile = open('dubdub.pkl','rb')
key = pickle.load(key_infile)
f = Fernet(key)
username = input("Username: ")
password = input("password: ")
website = input("Website: ")
e_username = f.encrypt(username.encode())
e_password = f.encrypt(password.encode())
e_list = ["Username: " + str(e_username), "Password: " + str(e_password)]
e_userpass["Website: " + website] = e_list
outfile = open("dubdub.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('dubdub.pkl','rb')
z = pickle.load(infile)
e_userpass = z
j = [e_userpass[k] for k in e_userpass]
for k in j:
    for q in k:
        f.decrypt(q)

"""for key, value in d_userpass.items():
    print(key, ' : ', value)"""