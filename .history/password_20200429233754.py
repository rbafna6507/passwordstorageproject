import pickle
import cryptography
from cryptography.fernet import Fernet

def newpass(website, username, password, key):
    passwords = {"Website: " + website: ("Username: " + username, "Password: "+ password)}
    e_username = encrypt(username, key)
    e_password = encrypt(password, key)
    e_userpass = {"Website: "+ website: ["Username: " + e_username, "Password: " + e_password]}
    outfile = open("passwords.pkl", "wb")
    pickle.dump(passwords, outfile)
    outfile.close()
    infile = open('passwords.pkl','rb')
    z = pickle.load(infile)

def deletepass(website, dictionary):
    if "Website: " + website in dictionary:
            del dictionary["Website: " + website]

def allpass(dictionary):
    print("These are Your Passwords:")
    for key, value in dictionary.items():
        print(key, ' : ', value)

def encrypt(message, key):
    return Fernet(key).encrypt(message)

def decrypt(token, key):
    return Fernet(key).decrypt(token)
