###############################
### PASSWORD AUTHENTICATION ###
###############################



# Welcome message
welcome = "Welcome to the University of Chester."
print(welcome)

# Username input
username = input("Please enter your username: ")

# Username & password check
if username != "Cyber":
    print(f"Username {username} is incorrect. Please restart.")
else:
    incorrect_password = True
    tries = 0

    while incorrect_password and tries < 3:
        password = input("Please enter your password: ")
        tries += 1
        if password != "Cyberp4ss":
            if tries < 3:
                print("Password is incorrect. Please try again.")
            else:
                print("Too many attempts. Program locked.")
        else:
            print("Validation successful.")
            incorrect_password = False