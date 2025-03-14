# Dictionaries take higher priority than a set.
# Sets are unordered, unique, mutable, and contain only immutable elements.



############
### SETS ###
############



a = {1, 1, 1, 1, 1, 2, 3, 4} # In this set, duplicate 1's are removed.
print(a)
print()

print("Are both sets the same? : ", {1, 2, 3} == {3, 2, 1}) # Ordering does not matter with sets; boolean will return True.
print("Are both lists the same? : ", [1, 2, 3] == [3, 2, 1]) # Ordering within a list does matter; will return false.
print()



# USAGE OF SETS FOR DUPLICATE REMOVAL #

# Initialising as list
letters = list("aabbccdd")
print("As a list:", letters)

# Converting to a set
letters = list(set(letters)) 
print("As a set:", letters)
print()



# SET THEORY #

c = {1, 2, 3, 4}
d = {3, 4, 5, 6} 

# Union
print("Union: ")
setUnion = c.union(d)
print(setUnion)
print(c | d) # Same result as above.
print()

# Intersection
print("Intersection:")
setIntersection = c.intersection(d)
print(setIntersection)
print(c & d) # Same result as above.
print()

# Symmetric difference
print("Symmetric difference:")
setSD = c.symmetric_difference(d)
print(setSD)
print(c ^ d) # Same result as above.
print()

# Difference
print("Difference:")
setDif = c.difference(d)
print(setDif)
print(c - d) # Same result as above.
print()

# Subsets and supersets
names = {"John", "Jo", "Ian", "Sarah", "Alex"}
group = {"Jo", "Ian"} # This is a subset of "names"; "names" being a superset of "group".
other = {"Jo", "Ann"}

print("Subsets & Supersets:")
print("Names - ", names)
print("Group - ", group)
print("Other - ", other)
print()
print("Boolean checks:")
print("Group is subset of names:", group.issubset(names)) # Boolean check.
print("Names is superset of group:", names.issuperset(group)) # "
print("Other is subset of names:", other.issubset(names)) # "
print("Other is superset of names:", other.issuperset(names)) # "
print()



# SET METHODS # 

c.add(5) # Adds an element.
x = c.copy() # Creates a copy of the set.
y = c # Creates a synonym to the set.
x.discard(4) # Remove element; no error if doesn't exist.
c.remove(3) # Remove element; error if doesn't exist.

print("Set 1 is", c)
print("Set 2 is", d)
print("Set 3 is", x)
print("Set 4 is", y)


def remove_duplicates(spells):
    spells = set(spells)
    unique_spells = []

    for item in spells:
        unique_spells.append(item)

    return unique_spells

