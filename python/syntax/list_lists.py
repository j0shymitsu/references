import random

name = "Josh"
age = "29"

list = []
list.append(name) # Places object at end of list.
list.insert(0, age) # Inserts object at specified index.
print(list)
print()



# FIBONACCI EXAMPLE #

fib = [0, 1, 1]

for x in range(30):
    next_num = fib[-1] + fib[-2]
    fib.append(next_num)

print(fib)
print()



# APPENDING AN ITEM TO A LIST WITHIN A LIST #

s = [[1,2,3], [4,5,6], [8,9,10]]
s[1].append(7)
print(s)
print()



# ROLLING A DICE #

die = [1, 2, 3, 4, 5, 6]
num = random.choice(die)
print(f"You rolled a {num}.")
print()



# PERFORMING A CYCLIC ROTATION OF A LIST #

l = [1, 2, 3, 4, 5]

for x in range(25):
    right = l.pop()
    l.insert(0, right)
    print(l)
print()



# EDITING LISTS #

lang = ["Python", "Swift", "C++", "Java", "C", "Rust"]
weblang = ["HTML", "CSS", "JavaScript", "PHP", "SQL"]

print(lang[-1]) # Print the last item.
print(lang[-3]) # Print the third from last item.
print(lang[2:5]) # Print index 2 to 5 (items 3 to 6).
print(lang[5:]) # Print from index 5 (item 6) to end.
print(lang[:]) # Print items beginning to end; creates shallow copy.
print()

lang.extend(weblang) # Extends object "lang" with all items within "weblang".
print("List after extend: ", lang)
print()

lang[2] = "C" # Inserts item "C" to index 2 within object "lang".
print("Updated list: ", lang)
print()

# Iterating through lists
for x in lang:
    print(x)
print()

# Boolean checks
print("Check for C in language list: ", "C" in lang)
print("Check for COBOL in language list: ", "COBOL" in lang)
print()

# Working with numbers
numbers = [n**2 for n in range(1, 6)]
print(numbers)
print()
    
# List slicing
    # my_list[start : stop : step] < syntax
scores = [50, 70, 30, 20, 90, 10, 50]
scores[1:5:2] # Slice from 1, up to (but not including) 5, every 2nd value
scores[:3] # Get all items from start up to (but not including) 3
scores[3:] # Get all items from index 3 to end
scores[::2] # Just the step function
scores[-1] # Gives last item
scores[-2] # Gives second last item
scores[-3:] # Gives last 3 items

# List concatenation
total = [1, 2, 3] + [4, 5, 6]

# Contains
fruits = ["apple", "orange", "banana"]
print("banana" in fruits) # returns True

# Delete
num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
del num_list[3] # Deletes item 4/index 3
del num_list[1:3] # Deletes item 2 up to (not inc) item 4
del num_list[:] # Deletes all elements 