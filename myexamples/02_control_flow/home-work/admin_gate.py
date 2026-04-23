username = input("Enter your username: ")

if username == "admin":
    password = input("Enter your password: ")
    if password == "secret":
        print("Access granted")
    else:
        print("Wrong password")
else:
    print("Unknown user")