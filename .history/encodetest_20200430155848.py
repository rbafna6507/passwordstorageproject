import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)

key = Fernet.generate_key()
infile = open('bruh.pkl','rb')
z = pickle.load(infile)
website = input("Website: ")
username = input("Username: ")
password = input("Password: ")
e_userpass = z
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)
e_userpass = {}
e_userpass["Website: " + website] = ["Username: " + str(e_username), "Password: " + str(e_password)]
outfile = open("bruh.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('bruh.pkl','rb')
z = pickle.load(infile)
e_userpass = z
print(e_userpass)
for value in e_userpass:
    str(value)
    bytes(value, "utf-8")
    decrypt(value, key)