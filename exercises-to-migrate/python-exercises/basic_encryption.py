###############################
### (VERY) BASIC ENCRYPTION ###
###############################



import math

# Converting to/from ASCII
print(ord("J"))    # "ord" converts character to ASCII.
print(str(ord("J"))   # Converting each ASCII to a string to avoid addition
     + " "
     + str(ord("o"))
     + " "
     + str(ord("s"))
     + " "
     + str(ord("h")))

print(chr(74)
      + chr(111)
      + chr(115)
      + chr(104))

# Message encryptor
message = input("\nEnter message to encrypt: ")
encrypted = ""

for letter in message:
    if letter == " ":
        encrypted += letter
    else:
        encrypted += (chr(ord(letter)**2))

print("\n")
print(f"Your message encrypted: {encrypted}\n\n")

# 2nd message encryptor w/ decryptor
message_2 = input("Enter another message to encrypt: ").upper()
encrypted_2 = ""

for letter in message_2:
    if letter == " ":
        encrypted_2 += letter
    else:
        encrypted_2 += (chr(ord(letter) * 4))

print(f"Encrypted message is: {encrypted_2}\n")

print("Now decrypting the code...")
decrypted = ""

for letter in encrypted_2:
    if letter == " ":
        decrypted += letter
    else:
        decrypted += (chr(round(ord(letter) / 4)))

print(f"Decrypted message is: {decrypted}")

