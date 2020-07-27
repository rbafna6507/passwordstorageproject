import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('dubdub.pkl','rb')
key = pickle.load(infile)
print(key)
print(type(key))