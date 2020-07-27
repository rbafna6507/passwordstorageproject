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

e_userpass = {
    "Youtube.com" : ["Username: " + str(e_username), "Password: " + str(e_password)]
}
outfile = open("test.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('test.pkl','rb')
z = pickle.load(infile)
print(z)
e_userpass = z
d_username = decrypt(e_username, key).decode()
d_password = decrypt(e_password, key).decode()
d_userpass = {
    "Youtube.com" : ["Username: " + str(d_username), "Password: " + str(d_password)]
}
print(d_userpass)