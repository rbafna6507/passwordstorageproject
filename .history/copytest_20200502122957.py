import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message: bytes, key: bytes) -> bytes:
    return Fernet(key).encrypt(message)

def decrypt(token: bytes, key: bytes) -> bytes:
    return Fernet(key).decrypt(token)


infile = open('jeff.pkl','rb')
z = pickle.load(infile)
key = Fernet.generate_key()
e_userpass = z
username = input("Username: ")
password = input("password: ")
website = input("Website: ")
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)
e_list = [b"Username: " + e_username, b"Password: " + e_password]
e_userpass["Website: " + website] = e_list
outfile = open("jeff.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('jeff.pkl','rb')
z = pickle.load(infile)
e_userpass = z
j = e_userpass.values()
for x in j:
    x.encode('utf-8')
    decrypt(x, key)

"""for key, value in d_userpass.items():
    print(key, ' : ', value)"""