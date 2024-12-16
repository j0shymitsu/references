password = input("Enter a password with at least ten characters: ")
while len(password) < 10:
    password = input("Password is too short. Please enter another: ")
else:
    print("Criteria met.\n")

password2 = input("Enter a second password between 10 and 15 characters: ")
while len(password2) <= 9 or len(password2) >= 16:
    password2 = input("Password doesn't meet requirements. Please enter another: ")
else:
    print("Criteria met.\n")

password3 = input("Enter a third password with 6 characters where the first character is a number: ")
while not(len(password3) == 6 and password3[0].isdigit()):
    password3 = input("Password doesn't meet requirements. Please enter another: ")
else:
    print("Criteria met.\n")

password4 = input("Enter a final password with a capital letter to start, and an even number of characters: ")
while not(len(password4) % 2 == 0 and password4[0].isupper()):
    password4 = input("Password doesn't meet requirements. Please enter another: ")
else:
    print("Criteria met.\n")
