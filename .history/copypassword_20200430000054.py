import pickle
import cryptography
from cryptography.fernet import Fernet

def newpass(website, username, password, key):
    e_username = encrypt(username.encode(), key)
    e_password = encrypt(password.encode(), key)
    e_userpass = {"Youtube.com" : ["Username: " + str(e_username), "Password: " + str(e_password)]}
    outfile = open("test.pkl", "wb")
    pickle.dump(e_userpass, outfile)
    outfile.close()
    infile = open('test.pkl','rb')
    z = pickle.load(infile)
    e_userpass = z
    d_username = decrypt(e_username, key).decode()
    d_password = decrypt(e_password, key).decode()
    d_userpass = {"Website: " + website: ["Username: " + str(d_username), "Password: " + str(d_password)]}
    print(d_userpass)

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

def command():
    global f
    f = str(input("Command: "))
    return f

key = Fernet.generate_key()
bruh = True

while bruh == True:
    command()
    if f== "n":
        website = input("Website: ")
        username = input("Username: ")
        password = input("Password: ")
        newpass(website, username, password, key)