import math
import random
import numpy as np
import time



#############
### LOOPS ### 
#############



print()

# Loop using range
print("Looping using range:")
for x in range(10, 0, -2):
    print(x)
print()

for x in range (1, 51, 1):
    print(x)
print()

for x in range (1, 51, 10):
    print(x)
print()

for x in range(50, 0, -1):
    print(x)
print()

x = int(input("Enter the times table: "))
print()
for i in range(1, 13):
    print(f"{i} x {x} = {i * x}")
print()

# Loop through a string
print("Looping through strings: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"
for letter in alphabet:
    if letter > "l":
        break
    else:
        print(letter)
print()

name = input("Please enter your name: ")
for letter in name:
    print(letter)
print()

# Nested loop
print("Nested loops:")
for i in range(3):
    for j in range(7, 10):
        print(i, j)



# ARRAYS #

array1d = np.array([1, 2, 4, 9, 16, 25])
array2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

# Print out 1d array
for df in array1d:
    print(df)
print()

# Print out 2d array
for x in array2d:
    print("Row: ", x)
    for y in x:
        print(y)
print()



# DICTIONARIES # 

my_dict = {"Josh":57, "Dave":55, "Sally":42, "Jim":99}

# Iterate through dictionary
for key, value in my_dict.items():
    print(key, ":", value)
    if value > 50:
        print(f"\tScore of {key} is {value-50} greater than 50.")
    else:
        print(f"\tScore of {key} didn't reach 50.")
print()


# ROLL A DIE # 

# Score keeper
josh = 0
opponent = 0
draw = 0

# Roll function
def roll(size):
    die = random.randint(1, size)
    return die

print("\n20 games of dice:\n\n")

# Loop
for i in range(20):

    joshRoll = roll(6)
    opponentRoll = roll(6)

    if joshRoll > opponentRoll:
        josh += 1
        print(f"Josh rolled: {joshRoll}\nOpponent rolled: {opponentRoll}\nJOSH WINS - current score is {josh}:{opponent} with {draw} draw(s).\n\n")
        time.sleep(1.5)
    elif opponentRoll > joshRoll:
        opponent += 1
        print(f"Josh rolled: {joshRoll}\nOpponent rolled: {opponentRoll}\nOPPONENT WINS - current score is {josh}:{opponent} with {draw} draw(s).\n\n")
        time.sleep(1.5)
    else:
        draw += 1
        print(f"Josh rolled: {joshRoll}\nOpponent rolled: {opponentRoll}\nDRAW - current score is {josh}:{opponent} with {draw} draw(s).\n\n")
        time.sleep(1.5)

# Results
print("\n\n")
print("*** FINAL RESULTS ***")
print()
print(f"Josh: {josh} | Opponent: {opponent} | Draws: {draw}.")
print()








