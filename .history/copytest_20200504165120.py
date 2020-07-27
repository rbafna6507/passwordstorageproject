import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token, key) -> bytes:
    return Fernet(key).decrypt(token)

e_userpass = {}
key_infile = open('dubdub.pkl','rb')
key = pickle.load(key_infile)
username = input("Username: ")
password = input("password: ")
website = input("Website: ")
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)
e_list = [e_username, e_password]
e_userpass["Website: " + website] = e_list
outfile = open("pass.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('pass.pkl','rb')
z = pickle.load(infile)
e_userpass = z
print(e_userpass)
j = [e_userpass[k] for k in e_userpass]
for k in j:
    for q in k:
        decrypt(q, key)
        print(q)