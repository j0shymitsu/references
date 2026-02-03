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
