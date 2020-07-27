import pickle
import cryptography
from cryptography.fernet import Fernet

def newpass(website, username, password, key, dictionary):
    username = key.encrypt(username.encode())
    password = key.encrypt(password.encode())
    infile = open("pass.pkl",'rb')
    dictionary = pickle.load(infile)
    dictionary[website]= [username, password]
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

def deletepass(delwebsite, dictionary):
    allpass()
    if "Website: " + delwebsite in dictionary:
        del dictionary["Website: " + delwebsite]
        outfile = open("pass.pkl", "wb")
        pickle.dump(dictionary, outfile)
        outfile.close()
        infile = open("pass.pkl",'rb')
        dictionary = pickle.load(infile)
        print("Deleted...")
    else:
        print("nope")

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

def command():
    global f
    f = str(input("Command: "))
    return f

bruh = True
v = {}

while bruh == True:
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
        del_website = input("Which Saved Password do You want to Delete?: ")
        deletepass(del_website, v)
    if f == "end":
        bruh = False
        print("You have ended your storage session.")
