list = True
dictionary = {}
while list == True:
    website = input("Website: ")
    username = input("Username: ")
    password = input("password: ")
    dictionary["Website: " + website] = [username, password]
    print(dictionary)