import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('dubdub.pkl','rb')
key = pickle.load(infile)
key = Fernet(key)
username = "Username"
password = "Password"
username = username.encode()
password = password.encode()
username = key.encrypt(username)
password = key.encrypt(password)
v = {"website": [username, password]}
outfile = open("test.pkl", "wb")
pickle.dump(v, outfile)
outfile.close()
infile = open('test.pkl','rb')
j = pickle.load(infile)
a = [j[k] for k in j]
for k in a:
    k[0] = key.decrypt(key[0])
    k[1] = password
        e = key.decrypt(e)
        e = e.decode()
"""a = key.decrypt(j)
e = a.decode()
print(e)"""