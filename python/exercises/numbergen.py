import random as ra

num = ra.randint(1, 10)
numOfGuesses = 1

while(True):
    guess = int(input("Guess a number between 1-10: "))

    if(guess < num):
        print("Incorrect! Try a higher number!\n")
        numOfGuesses += 1
    elif(guess > num):
        print("Incorrect! Try a lower number!\n")
        numOfGuesses += 1
    else:
        break

print()
print(f"CORRECT! The number was {num}!")
print(f"You took {numOfGuesses} guesses to get it correct.")
