import pickle

def newpass(website, username, password):
    passwords = {Website: " + website: ("Username: " + username, "Password: "+ password)}
    outfile = open("passwords.pkl", "wb")
    pickle.dump(passwords, outfile)
    outfile.close()
    infile = open('passwords.pkl','rb')
    z = pickle.load(infile)

def deletepass(website):
    if "Website: " + website in passwords:
            del passwords["Website: " + website]

def allpass(dictionary, file):
    dictionary = z = pickle.load(infile)