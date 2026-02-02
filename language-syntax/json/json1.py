import json
import pprint



############
### JSON ###
############



# Default list of dictionaries (JSON format):
visitors = {"Org": "University of Chester",
            "visitors": [{"name": "Test", "pass": 1234},
            {"name": "Josh", "pass": 4321}]}

# Printing/formatting:
print(visitors)
print()
pprint.pprint(visitors)     # "Pretty print" library; formats JSON data.

print(visitors["Org"])
print(visitors["visitors"])
print()

# Creating a new dictionary from existing:
visitor_dict = visitors["visitors"]
print(visitor_dict[0])      # Prints index 0 from new dict.
print()

# Choosing index:
print(visitors["visitors"][1]["name"])
print()

# Looping around the list:
print("ALL KEYS:")
for visitor_dict in visitors["visitors"]:
    print(f"Name: {visitor_dict['name']}  |  Code: {visitor_dict['pass']}")
    print()



# EXPORTING TO JSON #

# Assigning the filename:
filename = "json/visitors.json"

# Saving/overwriting the file:
try:
    with open(filename, "w") as f:      # "with open" defines the file you want to use; r=read, a=append, w=write.
        json.dump(visitors, f)
        print("Data written to JSON file.")
except:
    print("Error writing file: ", filename) 

# Reading the file:
try:
    with open(filename) as f:
        visitors = json.load(f)
except:
    print("Error reading file: ", filename)

print("\nThe loaded JSON now contains: ")
pprint.pprint(visitors)
print()


