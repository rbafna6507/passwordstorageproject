import pickle

def newpass(website, username, password):
    passwords = {
        "Website; " + website: ("Username: " + username, "Password: "+ password)
        outfile = open("passwords.pkl", "wb")
        pickle.dump(passwords, outfile)
        outfile.close()
        infile = open('passwords.pkl','rb')
        global z
        z = pickle.load(infile)
    }