import pickle
import cryptography
from cryptography.fernet import Fernet

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)

key = Fernet.generate_key()
website = input("Website: ")
username = input("Username: ")
password = input("Password: ")
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)
e_userpass = {}
e_userpass["Website: " + website] = ["Username: " + str(e_username), "Password: " + str(e_password)]
outfile = open("qqq", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('qqq.pkl','rb')
z = pickle.load(infile)
e_userpass = z
print(type(e_userpass))