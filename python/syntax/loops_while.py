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
