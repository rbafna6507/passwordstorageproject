import pickle
import cryptography
from cryptography.fernet import Fernet

def newpass(website, username, password, key, dictionary):
    username = key.encrypt(username.encode())
    password = key.encrypt(password.encode())
    infile = open("pass.pkl",'rb')
    dictionary = pickle.load(infile)
    dictionary["Website: " + website]= [username, password]
    outfile = open("pass.pkl", "wb")
    pickle.dump(dictionary, outfile)
    outfile.close()
    infile = open("pass.pkl",'rb')
    dictionary = pickle.load(infile)
    a = [dictionary[k] for k in dictionary]
    for k in a:
        k[0] = key.decrypt(k[0]).decode()
        k[1] = key.decrypt(k[1]).decode()
    print(dictionary)
    print("\n")

def deletepass(delpass, dictionary):
    infile = open('pass.pkl','rb')
    dictionary = pickle.load(infile)
    if "Website: " + delpass in dictionary:
        del dictionary["Website: " + delpass]
        outfile = open("pass.pkl", "wb")
        pickle.dump(dictionary, outfile)
        outfile.close()
        infile = open('pass.pkl','rb')
        dictionary = pickle.load(infile)
        print("Deleted...")
        allpass()
        print("\n")
    else:
        print("NOPE")

def allpass():
    print("These are Your Passwords:")
    infile = open("pass.pkl",'rb')
    dictionary = pickle.load(infile)
    a = [dictionary[k] for k in dictionary]
    key_infile = open('dubdub.pkl','rb')
    key = pickle.load(key_infile)
    key = Fernet(key)
    for k in a:
        k[0] = key.decrypt(k[0]).decode()
        k[1] = key.decrypt(k[1]).decode()
    for key, value in dictionary.items():
        print(key, ' : ', value)
    print("\n")

def command():
    global f
    f = str(input("Command: "))
    return f

rand_bool = True
v = {}

while rand_bool == True:
    key_infile = open('dubdub.pkl','rb')
    key = pickle.load(key_infile)
    key = Fernet(key)
    command()
    if f== "n":
        website = str(input("Website: "))
        username = "Username: " + input("Username: ")
        password = "Password: " + input("Password: ")
        newpass(website, username, password, key, v)
    if f == "a":
        allpass()
    if f== "k":
        allpass()
        del_website = input("Which Saved Password do You want to Delete?: ")
        deletepass(del_website, v)
    if f == "end":
        rand_bool = False
        print("You have ended your storage session.")
