numbers = [10, 20, 20, 20, 30, 40, 50]

names = ["Bob", "Louise", "Sarah", "Fred", "Bob"]

numbers_tuple = (10, 20, 30, 40, 40)

print(numbers)
print(names)
print(numbers_tuple)
print()

numbers[0] = 100 # Changes index 0 (first element)
print(numbers)
print()

numbers.append(60) # Adds a single element to end of list
print(numbers)
print()

numbers.insert(0, "Zero") # Adds a single element to specified index
print(numbers)
print()

numbers.extend([60, 70, 80, 90]) # Adds each item from an iterable to the end of a list
print(numbers)
print()

removed_elem = numbers.pop() # Removes last element from list and stores in new var
print(numbers)
print(removed_elem)
print()

first_elem = numbers.pop(0) # Removes element from index 0 and stores in new var
print(numbers)
print(first_elem)
print()

numbers.remove(40) # Removes specified element from list
print(numbers)
print()

x = numbers.count(20) # Counts the instances of specified element
print(f"The instances of the number 20 are {x}.")
print()

y = numbers.index(70) # Searches the index of specified value
print(f"The index of the number 70 is {y}.")
print()


# Searching a list for a value

elem = 20 # Sets the value
elem_position = [] # Initialises empty list to store indices
i = 0

for a in numbers:
    if a == elem:
        elem_position.append(i)
    i += 1
print(f"The number {elem} has been found {len(elem_position)} times at these indices {elem_position}")
print()


# Working with lists

order = ['Big Mac', 'Fries', 'Milkshake']
item = order[2]
print(f"Item number 3 is {item}.")
print()


cities = ['Chester','London', 'Liverpool', 'Glasgow']
print(f"The length of the list of cities is {len(cities)}.")
print(f"The first city alphabetically is {min(cities)}, the last alphabetically is {max(cities)}.")
print()

stations = ["Upton", "Heswall", "Neston", "Shotton", "Hawarden", "Wrexham"]
print(f"The number of stations is {len(stations)}. The train will be stopping at {stations}")
print()

print(f"The first stop is {stations[0]} - The last stop is {stations[-1]}")
print()

stations.insert(3, "Hawarden Bridge")
print(f"The updated journey is: {stations}")
print()

stations.pop()
print(f"The train will now be terminating at {stations[-1]}")










