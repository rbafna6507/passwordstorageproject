list = True
dictionary = {}
while list == True:
    website = input("Website: ")
    username = input("Username: ")
    password = input("password: ")
    dictionary["Website: " + website] = [username, password]
    for key, value in e_userpass.items():
        print(key, ' : ', value)