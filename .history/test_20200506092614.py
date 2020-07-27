import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('pass.pkl','rb')
j = pickle.load(infile)
print(j)
delpass = input("Password to delete")
if "Website: " + delpass in j:
    del j["Website: " + delpass]