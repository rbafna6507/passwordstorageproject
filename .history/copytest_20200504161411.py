import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)

e_userpass = {}
key_infile = open('dubdub.pkl','rb')
key = pickle.load(key_infile)
username = input("Username: ")
password = input("password: ")
website = input("Website: ")
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode())
e_list = ["Username: " + str(e_username), "Password: " + str(e_password)]
e_userpass["Website: " + website] = e_list
outfile = open("pass.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('pass.pkl','rb')
z = pickle.load(infile)
e_userpass = z
j = [e_userpass[k] for k in e_userpass]
for k in j:
    for q in k:
        key.decrypt(q)
        print(q)

"""for key, value in d_userpass.items():
    print(key, ' : ', value)"""