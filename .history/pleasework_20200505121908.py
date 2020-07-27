import pickle
import cryptography
from cryptography.fernet import Fernet

key_infile = open('dubdub.pkl','rb')
key = pickle.load(key_infile)
infile = open("test.pkl", "rb")
v = pickle.load(infile)
key = Fernet(key)
username = "Username: " + input("Username: ")
password = "Password: " + input("Password: ")
username = username.encode()
password = password.encode()
username = key.encrypt(username)
password = key.encrypt(password)
username2 = "username"
username2 = username2.encode()
username2 = key.encrypt(username2)
password2 = "password"
password2 = password2.encode()
password2 = key.encrypt(password2)
v["website"]= [username, password]
outfile = open("test.pkl", "wb")
pickle.dump(v, outfile)
outfile.close()
infile = open('test.pkl','rb')
j = pickle.load(infile)
a = [j[k] for k in j]
for k in a:
    k[0] = key.decrypt(k[0])
    k[1] = key.decrypt(k[1])
    k[0] = k[0].decode()
    k[1] = k[1].decode()
print(j)
"""a = key.decrypt(j)
e = a.decode()
print(e)"""