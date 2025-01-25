import math # Imports math library; can be declared anywhere in code.

### OPERATORS ###

# Define a string
x = "Hello Josh"
print(x)
print("\n")

# Concatenating strings
print(x + ", my name is Python")
print("\n")

# Boolean conditions
print("Josh" in x)
print("Cyber" in x)
print("\n")

# The same in "if" statements
if "Josh" in x:
    print("Yes, 'Josh' is present.")
if "Cyber" not in x:
    print("No, 'Cyber' is NOT present.")
print("\n")

# Change a string
print(x.upper())
print(x.lower())
print(x.split())
print("\n")

# Change a string value
x = x + ", welcome to Python"
print(x)
print("\n")

# Print the length of a string
print(len(x))
print("\n")

# String slicing
print(x[0]) # First character.
print(x[1]) # Second character.
print(x[-1]) # Last character.
print(x[-4]) # Fourth from last character.
print(x[0:7]) # First 7 characters not including [7].
print(x[2:]) # Second character onwards not including [1].
print(x[:]) # All.
print("\n")

# Mathematical operators
a = 20
b = 25
c = 5
d = 1.024e18 # Scientific notation

print(a+b) # Add two numbers.
print(a-b) # Subtract two numbers.
print(a*b) # Divide two numbers.
print(a//b) # Floor division
print(a**b) # Exponent
print("\n")

a = a+1 # Add 1 to "a".
print(a)
a += 1 # Increment "a" by 1.
print(a)
print("\n")

print(c**2) # "c" squared
print(math.sqrt(144)) # Square root; division will always present a float.

# More literal example
hours = 35.0
rate = 12.50
pay = hours * rate
print(pay)
print("\n")

## Numeric Expressions
xx = 2
xx = xx + 2
print(xx)

yy = 440 * 12
print(yy)

zz = yy / 1000
print(zz)

jj = 23
kk = jj % 5
print(kk)

print(4 ** 3)



### MATHEMATICAL OPERATORS ###

a = 20
b = 25
c = 5

print(a + b) # Add two numbers.
print(a - b) # Subtract two numbers.
print(b * a) # Multiply two numbers.
print(b / a) # Divide two numbers.

a = a + 1 # Increment "a" by 1.
print(a)

a += 1 # Increment "a" by 1.
print (a)

a -= 1 # Decrement "a" by 1.
print(a)

print(c**2) # Square of "c".

# Square root needs the math library
import math
print(math.sqrt(9))

# Python allows underscores for delimiters
num = 16_000
num = 16_000_000
print(num)

## Representing a number in binary
print(0b0001)
print(0b0101)