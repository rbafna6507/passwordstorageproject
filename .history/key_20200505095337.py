import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('dubdub.pkl','rb')
key = pickle.load(infile)
key = Fernet(key)
v = {"website": ["Username", "Password"]}
k = v.encode()
j = key.encrypt(k)
outfile = open("test.pkl", "wb")
pickle.dump(j, outfile)
outfile.close()
infile = open('test.pkl','rb')
j = pickle.load(infile)
a = key.decrypt(j)
e = a.decode()
print(e)
