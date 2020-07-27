import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('dubdub.pkl','rb')
key = pickle.load(infile)
key = Fernet(key)
v = "password"
j = key.encrypt(v)
outfile = open("test.pkl", "wb")
pickle.dump(v, outfile)
outfile.close()
infile = open('test.pkl','rb')
v = pickle.load(infile)
print(key)
