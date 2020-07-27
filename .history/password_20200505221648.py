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

def deletepass(website):
    allpass()
    if "Website: " + website in v:
        del v["Website: " + website]
        outfile = open("pass.pkl", "wb")
        pickle.dump(v, outfile)
        outfile.close()
        infile = open("pass.pkl",'rb')
        v = pickle.load(infile)
        print("Deleted...")

def allpass():
    print("These are Your Passwords:")
    infile = open("pass.pkl",'rb')
    v = pickle.load(infile)
    for key, value in v.items():
        print(key, ' : ', value)

def command():
    global f
    f = str(input("Command: "))
    return f

bruh = True

while bruh == True:
    key_infile = open('dubdub.pkl','rb')
    key = pickle.load(key_infile)
    key = Fernet(key)
    command()
    if f== "n":
        username = "Username: " + input("Username: ")
        password = "Password: " + input("Password: ")
        website = input("Website: ")
        newpass(website, username, password, key)
    if f == "a":
        allpass()
    if f== "k":
        del_website = input("Which Saved Password do You want to Delete?: ")
        deletepass(del_website)
    if f == "end":
        bruh = False
        print("You have ended your storage session.")
