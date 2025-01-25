# Defining a string
x = "Hello"
print(x, "\n")

# Concatenating strings
print(x + ", my name is Josh")

# Boolean conditions returning true or false
print("Josh" in x)
print("Hello" in x)

# Changing a string
print(x.upper()) # Uppercase
print(x.lower()) # Lowercase

# Changing a string value
x = x + ", welcome to Python"
print(x)

# Splitting a string
print(x.split())

print() # Printing an empty line

# String slicing
print(x[0]) # Index 0 (first character)
print(x[1]) # Index 1 (second character)
print(x[-1]) # Last character
print(x[-2]) # Second to last character
print(x[0:5]) # First 5 (not including [5])
print(x[2:]) # Second character onwards (not including [2])
print(x[:]) # All

print()

while x == "Josh, welcome to Python":
    print(x[0:1])
    print(x[0:2])
    print(x[0:3])
    print(x[0:4])
    print(x[0:5])
    print(x[0:6])
    print(x[0:7])
    print(x[0:8])
    print(x[0:9])
    print(x[0:10])
    print(x[0:11])
    print(x[0:12])
    print(x[0:13])
    print(x[0:14])
    print(x[0:15])
    print(x[0:16])
    print(x[0:17])
    print(x[0:18])
    print(x[0:19])
    print(x[0:20])
    print(x[0:21])
    print(x[0:22])
    print(x[0:23])
    print(x[0:23])
    print(x[0:22])
    print(x[0:21])
    print(x[0:20])
    print(x[0:19])
    print(x[0:18])
    print(x[0:17])
    print(x[0:16])
    print(x[0:15])
    print(x[0:14])
    print(x[0:13])
    print(x[0:12])
    print(x[0:11])
    print(x[0:10])
    print(x[0:9])
    print(x[0:8])
    print(x[0:7])
    print(x[0:6])
    print(x[0:5])
    print(x[0:4])
    print(x[0:3])
    print(x[0:2])
    print(x[0:1])

###

### COFFEE SHOP EXAMPLE ###

name = input("Please enter your full name: ")
print()

p1 = name.find(" ")
forename = name[:p1]
p2 = name.find(" ", p1+1)

# Checking if there is a middle name
if p2 != -1:
    middleName = name[p1+1:p2]
    p3 = name.find(" ", p2+1)
    if p3 != -1:
        surname = name[p2+1:p3]
    else:
        surname = name[p2+1:]
else:
    middleName = "N/A"
    surname = name[p1+1:]

print("Forename:", forename)
print("Middle name:", middleName)
print("Surname:", surname)
print()

icedCoffee = input("Are you ordering iced coffee? > ").lower()
if icedCoffee in ["y", "yes"]:
    icedCoffee = input("Please enter the number of iced coffees being purchased: ")
    print()

    icedCoffee = int(icedCoffee)
    total = icedCoffee * 2.95
    VAT = 0
    profit = icedCoffee * 1.95

    print("Total cost: £{:0.2f}".format(round(total, 2)))
    print("Total VAT paid: £{:0.2f}".format(round(VAT, 2)))
    print("Total profit to coffee shop: £{:0.2f}".format(round(profit, 2)))

else:
    coffee = input("Please enter the number of coffees being purchased: ")
    print()

    coffee = int(coffee)
    total = coffee * 2.95
    VAT = total - (total / 1.2)
    profit = coffee * 1.95

    print("Total cost: £{:0.2f}".format(round(total, 2)))
    print("Total VAT paid: £{:0.2f}".format(round(VAT, 2)))
    print("Total profit to coffee shop: £{:0.2f}".format(round(profit, 2)))


###

# Asking user for their name
name = input("Please enter your full name: ").strip().title()

# Removing whitespace from str and capitalising users name; strung together
nameCaps = name.strip()

# Capitalizing first letter
nameCap1 = name.capitalize()

# Capitalizing each word
name = name.title()

# Splitting users name into first and last name
first, last = name.split(" ")

# Saying hello to user
print("Hello, ", end="") # "end" overrides the default value (/n); below (new line in code) will stay on same line.
print(name)

print("Hello, \"friend\"") # \ = A return function to print symbols.

print(f"hello, {name}") # Format string or "fstring".

# print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)

