import pickle
import cryptography
from cryptography.fernet import Fernet


def newpass(website, username, password, key):
    infile = open("test.pkl", "rb")
    v = pickle.load(infile)
    username = key.encrypt(username.encode())
    password = key.encrypt(password.encode())
    v[website]= [username, password]
    outfile = open("test.pkl", "wb")
    pickle.dump(v, outfile)
    outfile.close()
    infile = open('test.pkl','rb')
    v = pickle.load(infile)
    a = [v[k] for k in v]
    for k in a:
        k[0] = key.decrypt(k[0]).decode()
        k[1] = key.decrypt(k[1]).decode()
    print(v)

def deletepass(website):
    print("Here are your Passwords")
    allpass()
    if "Website: " + website in v:
        del v["Website: " + website]
        outfile = open("test.pkl", "wb")
        pickle.dump(v, outfile)
        outfile.close()
        print("Deleted...")

def allpass():
    print("These are Your Passwords:")
    for key, value in v.items():
        print(key, ' : ', value)

def command():
    global f
    f = str(input("Command: "))
    return f

v = {}
bruh = True

while bruh == True:
    key_infile = open('dubdub.pkl','rb')
    key = pickle.load(key_infile)
    key = Fernet(key)
    infile = open('test.pkl','rb')
    v = pickle.load(infile)
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
