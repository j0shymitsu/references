import math
import random
import numpy as np



#################
### FUNCTIONS ###
#################



# # Function to say hello to a list of users
# def hello(x):
#     print(f"hi {x}")

# names = ["Josh", "Alan", "Ben", "Carl"]

# for n in names:
#     hello(n)
# print()

# # Function to calculate the power of a number
# def power(x, y):
#     return x ** y

# z = power(4, 3)
# print(z)
# print()

# # Function for a short greeting
# def greeting(name):
#     print(f"Hello {name}, how are you today?")

# name = (input("Hello! Plese enter your name: "))
# greeting(name)
# print()



# # DICE GAME #

# rollFreq = {}

# # Function for dice roll
# def roll(size):
#     die = random.randint(1, size)
#     x = rollFreq.setdefault(die, 0)
#     rollFreq[die] = x + 1
#     print("Rolled: ", die)
#     return die

# print("Dice roller!")
# print()
# for i in range(20): # Rolls 20x.
#     myTurn = roll(6) + roll(6)
#     print("You rolled a total of: ", myTurn)
#     print()

# print("Roll frequencies =", rollFreq)
# print()



# # FIND THE MAX OF 3 NUMBERS #

# def max3(a, b, c):
#     numbers = [a, b, c]
#     largest = max(numbers)
#     count = numbers.count(largest)

#     if count > 1:
#         print(f"There are {count} numbers that are the largest at {largest}")
#     return largest
    
# a = int(input("Please enter number a: "))
# b = int(input("Please enter number b: "))
# c = int(input("Please enter number c: "))

# largest = max3(a, b, c)
# print(f"The largest number in the list is {largest}")
# print()



# # SUM OF ALL NUMBERS # 

# nums = []

# def sumup(x):
#     for i in range(0, x):
#         n = random.randint(1, 51)
#         nums.append(n)
#     print(f"Your numbers are {nums}, and their total sum is:", sum(nums))

# totalsum = int(input("Enter how many random numbers up to 50 would you like to sum up: "))
# sumup(totalsum)
# print



# # PRODUCT OF ALL NUMBERS # 

# nums2 = []

# def prod(x):
#     for i in range (0, x):
#         n = random.randint(1, 51)
#         nums2.append(n)
#     print(f"Your numbers are {nums2}, and their product is", np.prod(nums2))

# total = int(input("Enter the amount of random numbers up to 50 would you like to multiply: "))
# prod(total)
# print()    



# # REVERSE TEXT #

# def reverser(x):
#     reversetext = x[::-1]
#     print(reversetext)

# text = input("Please enter a string: ")
# print("Your text reversed: ")
# reverser(text)
# print()



# # CALCULATE FACTORIAL #

# def factorial(x):
#     ans = 1
#     for i in range (1, x+1):
#         ans = ans * i
#         print(ans)

# x = int(input("Please enter a number to calculate it's factorial: "))
# print()
# factorial(x)



# OTHER FUNCTIONS #

# Standard syntax:
def f():
    s = "-- Inside f()"
    print(s)

print("Before calling f()")
f()
print("After calling f()")
print()

# Stub:
def g():
    pass
print()

# Positional arguments:
def shop(qty, item, price):
    print(f"{qty} {item} cost £{price:.2f}")

shop(6, "bananas", 1.74)
print()
