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



# WHILE LOOPS #

# Capacity checker
print("Capacity checker:")
capacity = 4
players = 0

while players < capacity:
    entry = int(input("Enter(1) or Exit(-1) : "))
    players += entry
    print(f"Capacity is now at {players}. {capacity - players} spaces remaining.")
print("Game is full. No more players.")
print()

# Letter guessing game
print("Letter guessing game:")
letter = "a"
guesses = 0

while True:
    guesses += 1
    x = input("Guess what letter I'm thinking of (a-z): ")
    if x == letter:
        break
    print("Try again!")

print(f"\nCorrect, I was thinking of the letter {letter}.")
print(f"You had {guesses} attempts.")
print()

# Random number guessing game
print("Number guessing game:")
numlist = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
num = random.choice(numlist)

while True:
    guess = int(input("Guess what number I'm thinking of between 1 and 10: "))
    print()
    if guess == num:
        break
    print("Try again!")
    print()

print(f"Correct, the number was {num}.")



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








