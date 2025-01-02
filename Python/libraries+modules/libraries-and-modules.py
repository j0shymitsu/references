from dice import Dice   # Accesses a library/module/file, in this case, one I've created.



#####################################
### ACCESSING LIBRARIES & MODULES ###
#####################################



# DICE GAME #

dice1 = Dice(6, "Red")  # Accesses class from other file
dice2 = Dice(6, "Blue")

a = dice1.roll()     # Method that belongs to dice
b = dice2.roll()
print()

print(f"Red dice rolled: {a}")
print(f"Blue dice rolled: {b}")
print()

if a > b:
    print(dice1, "wins.")
elif b > a:
    print(dice2, "wins.")
else:
    print("Draw.")

