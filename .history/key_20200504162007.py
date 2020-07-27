import pickle
import cryptography
from cryptography.fernet import Fernet

key = Fernet.generate_key()
outfile = open("dubdub.pkl", "wb")
pickle.dump(key, outfile)
outfile.close()
infile = open('dubdub.pkl','rb')
key = pickle.load(infile)
print(key)
print(type(key))