import pickle
import cryptography
from cryptography.fernet import Fernet

v = {}

def pickleit():
    outfile = open("test.pkl", "wb")
    pickle.dump(v, outfile)
    outfile.close()
    global infile
    infile = open('test.pkl','rb')

def newpass(website, username, password, key):
    infile = open("test.pkl", "rb")
    v = pickle.load(infile)
    key = Fernet(key)
    username = key.encrypt(username.encode())
    password = key.encrypt(password.encode())
    v[website]= [username, password]
    pickleit()
    j = pickle.load(infile)
    a = [j[k] for k in j]
    for k in a:
        k[0] = key.decrypt(k[0]).decode()
        k[1] = key.decrypt(k[1]).decode()
    print(j)

def deletepass(website):
    if "Website: " + website in v:
            del v["Website: " + website]
            pickleit()

def allpass():
    print("These are Your Passwords:")
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
