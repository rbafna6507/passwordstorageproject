import pickle
import cryptography
from cryptography.fernet import Fernet
infile = open('test.pkl','rb')
z = pickle.load(infile)
website = input("Website: ")
username = input("Username: ")
password = input("Password: ")
e_userpass = z
e_username = encrypt(username.encode(), key)
e_password = encrypt(password.encode(), key)
e_userpass = {}
e_userpass["Website: " + website] = ["Username: " + str(e_username), "Password: " + str(e_password)]
outfile = open("test.pkl", "wb")
pickle.dump(e_userpass, outfile)
outfile.close()
infile = open('test.pkl','rb')
z = pickle.load(infile)
e_userpass = z
print(e_userpass)
d_username = decrypt(e_username, key).decode()
d_password = decrypt(e_password, key).decode()
d_userpass = {"Website: " + website: ["Username: " + str(d_username), "Password: " + str(d_password)]}
print(d_userpass)