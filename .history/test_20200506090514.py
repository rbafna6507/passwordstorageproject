import pickle
import cryptography
from cryptography.fernet import Fernet

infile = open('test.pkl','rb')
j = pickle.load(infile)