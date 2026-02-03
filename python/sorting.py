### IN-PLACE SORTING ###



letters = ["A", "C", "D", "M", "B", "L"]
letters.reverse() # Sort in reverse order; methods change original lists
print(f"First set of letters in reverse are {letters}")
print()

letters2 = ["X", "Z", "M", "N", "U", "R"]
s = sorted(letters2) # Functions keep original list the same
print(f"Second set of letters after sorting are {s}")
print()

s = reversed(letters) # Out-of-place sort in reverse order
print(f"First set of letters after reverse sorting {list(s)}")
print()
print(f"Original list is {letters}")
print()

firstname = "Josh"
name = list(firstname)
print(name)
print()

for letter in name:
    print(letter.upper(), end="") # "end=""" puts all items on same line