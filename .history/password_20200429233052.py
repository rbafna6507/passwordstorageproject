import pickle
import cryptography
from cryptography.fernet import Fernet

def newpass(website, username, password):
    passwords = {"Website: " + website: ("Username: " + username, "Password: "+ password)}
    outfile = open("passwords.pkl", "wb")
    pickle.dump(passwords, outfile)
    outfile.close()
    infile = open('passwords.pkl','rb')
    z = pickle.load(infile)

def deletepass(website, dictoinary):
    if "Website: " + website in passwords:
            del passwords["Website: " + website]

def allpass(dictionary, file):
    dictionary = file
    print(dictionary)

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)
