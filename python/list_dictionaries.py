# Dictionaries cannot have duplicate keys.
# Looking up an item from a list takes linear time - Dictionaries are more useful in terms of speed.



####################
### DICTIONARIES ###
####################



# Initialising blank dictionary
a_blank_dict = {}
print(type(a_blank_dict)) # Checked with the type() function.
print()

# Dictionaries for country population
countries = {
    "UK":67000000,
    "France":65000000,
    "Spain":47000000,
    "Italy":59000000,
}

countries_2 = {
    "Belgium":12000000,
    "Sweden":10000000,
    "Norway":5000000,
}

print("COUNTRIES\n")



# INPUT 

x = input("Which country would you like to know the population of? UK, France, Spain, Italy, or Australia? : ")

# Inserting a missing country
countries["Australia"] = 20000000

# if/else check
if x == "UK":
    print(countries["UK"])
elif x == "France":
    print(countries["France"])
elif x == "Spain":
    print(countries["Spain"])
elif x == "Italy":
    print(countries["Italy"])
elif x == "Australia":
    print(countries["Australia"])
else:
    print("Please choose a country from the list.")
print()



# INFO READ #

# Extracting the keys
print(countries.keys())

# Creating neater list of current keys
countryNames = list(countries.keys())
print(countryNames)
print()

# Excracting the country and pop info
print(countries.keys())
countryNames = list(countries.keys())
print(countryNames)
print()

print(countries.values())
population = list(countries.values())
print(population)
print()

print(countries.items())
countryPop = list(countries.items()) # Contains a tuple.
print(countryPop)
print()



# LISTING #

for cp in countryPop:
    print(cp[0], cp[1]) # Indices indicating key/value pair.
print()

for cp in countryPop:
    print(f"The country {cp[0]} has a population of {cp[1]}.") # Neater.
print()

# Targeting a specific key/value
print("The population of the UK is", countries.get("UK"))
print()

# Removing a specific key/value
removedElem = countries.pop("UK")
print("Removed country", removedElem)
print("The dictionary is now", countries)
print()

removedElem2 = countries.popitem()
print("Value of the popped key is", removedElem2)
print("The dictionary now is", countries)
print()

print(f"The population of France is", countries.get("France"))
print()

# Checking value; if key not present, inserting key
countries.setdefault("Iceland", 400000)
print(countries)
print("\n\n")



# UPDATING #

print("SCORES\n")

scores = {
    "Alan":67,
    "Bob":71,
    "Carl":66,
    "David":81,
    "Ethan":79
}
print(scores)
print()

scores["Frank"] = 50 # Adds a new key/value pair.
print(scores)
print()

scoreUpdate = scores.get("Alan")
scores["Alan"] = scoreUpdate +1
print(scores)
print()

scores.setdefault("Gareth", 55) # Adds a new key/value pair whilst avoiding overwriting.
print(scores)
print()
scores.setdefault("Harry", 90)
print(scores)
print()

del scores["Alan"]    # Removes the key and value pair

# iterating over a dictionary
def get_most_common_enemy(enemies_dict):
    max_so_far = float("-inf")
    max_name = None

    for name in enemies_dict:
        count = enemies_dict[name]
        if count > max_so_far:
            max_so_far = count
            max_name = name

    return max_name

# more iterating functions
def merge(dict1, dict2):
    new_dict = {}
    
    for quarter in dict1:
        score = dict1[quarter]
        new_dict[quarter] = score

    for quarter in dict2:
        score = dict2[quarter]
        new_dict[quarter] = score

    return new_dict


def total_score(score_dict):
    total = 0
    for quarter in score_dict:
        score = score_dict[quarter]
        total += score

    return total