import pickle
import cryptography
from cryptography.fernet import Fernet

def pickleit():
    outfile = open("test.pkl", "wb")
    pickle.dump(v, outfile)
    outfile.close()
    infile = open('test.pkl','rb')

def newpass(website, username, password, key):
    infile = open("test.pkl", "rb")
    v = pickle.load(infile)
    key = Fernet(key)
    username = key.encrypt(username.encode())
    password = key.encrypt(password.encode())
    v[website]= [username, password]
    a = [j[k] for k in j]
    for k in a:
        k[0] = key.decrypt(k[0]).decode()
        k[1] = key.decrypt(k[1]).decode()
    print(j)

def deletepass(website, dictionary):
    if "Website: " + website in dictionary:
            del dictionary["Website: " + website]

def allpass(dictionary):
    print("These are Your Passwords:")
    for key, value in dictionary.items():
        print(key, ' : ', value)

def command():
    global f
    f = str(input("Command: "))
    return f

key = Fernet.generate_key()
bruh = True

while bruh == True:
    key_infile = open('dubdub.pkl','rb')
    key = pickle.load(key_infile)
    command()
    if f== "n":
        username = "Username: " + input("Username: ")
        password = "Password: " + input("Password: ")
        website = input("Website: ")
        newpass(website, username, password, key)
